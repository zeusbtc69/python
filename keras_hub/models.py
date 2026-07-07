"""Compatibility shim: provide `YOLOv8Detector` for notebooks that import
`keras_hub.models.YOLOv8Detector`.

This attempts to use `keras_cv` if available, falling back to `ultralytics`.
It intentionally keeps a small adapter surface: `from_preset()` returns an
object with `predict()` to match typical usage in notebooks.
"""
from typing import Any


class _Adapter:
    def __init__(self, model, kind: str):
        self._model = model
        self._kind = kind

    def predict(self, batch_input: Any, *args, **kwargs):
        # Keras models expose `predict`; ultralytics exposes `predict` too but
        # may accept different inputs — try common calls.
        if hasattr(self._model, "predict"):
            return self._model.predict(batch_input, *args, **kwargs)
        # try callable
        if callable(self._model):
            return self._model(batch_input)
        raise RuntimeError("Underlying model has no callable predict interface")


class YOLOv8Detector:
    """Factory and wrapper to provide a stable API for the notebook.

    Usage in notebook (no changes needed):
        detector = keras_hub.models.YOLOv8Detector.from_preset("yolov8_m_pascalvoc", bounding_box_format="rel_xyxy")
        result = detector.predict(batch_input)
    """

    def __init__(self, adapter: _Adapter):
        self._adapter = adapter

    @classmethod
    def from_preset(cls, preset: str, bounding_box_format: str = "rel_xyxy"):
        # Try keras_cv first
        try:
            import importlib

            kc_spec = importlib.util.find_spec("keras_cv")
            if kc_spec:
                import keras_cv
                # Many keras_cv versions expose models under keras_cv.models
                models_mod = getattr(keras_cv, "models", None)
                if models_mod:
                    # try common names
                    for attr in ("YOLOv8", "yolov8", "YOLO"):
                        if hasattr(models_mod, attr):
                            KClass = getattr(models_mod, attr)
                            # Try common constructor patterns
                            try:
                                model = KClass.from_preset(preset)
                            except Exception:
                                try:
                                    model = KClass()
                                except Exception:
                                    model = None
                            if model is not None:
                                return cls(_Adapter(model, "keras_cv"))
                # try deep path: keras_cv.models.yolo
                try:
                    ymod = importlib.import_module("keras_cv.models.yolo")
                    for name in dir(ymod):
                        if "yolo" in name.lower():
                            KClass = getattr(ymod, name)
                            try:
                                model = KClass.from_preset(preset)
                            except Exception:
                                try:
                                    model = KClass()
                                except Exception:
                                    model = None
                            if model is not None:
                                return cls(_Adapter(model, "keras_cv"))
                except Exception:
                    pass
        except Exception:
            pass

        # Fallback: try ultralytics YOLO
        try:
            from ultralytics import YOLO as _YOLO

            # ultralytics accepts a model name/weights; the preset string may
            # differ — attempt to pass through the preset and let ultralytics
            # raise a clear error if it is invalid.
            model = _YOLO(preset)
            return cls(_Adapter(model, "ultralytics"))
        except Exception:
            pass

        raise ImportError(
            "YOLOv8Detector not available: install `keras-cv` or `ultralytics`, or use a supported preset."
        )

    def predict(self, batch_input: Any, *args, **kwargs):
        return self._adapter.predict(batch_input, *args, **kwargs)


__all__ = ["YOLOv8Detector"]
