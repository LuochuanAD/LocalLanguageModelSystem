import yaml
from pathlib import Path
from .schema import ModelConfig, RuntimeConfig

class ConfigLoader:
    _config = {}
    _last_mtime = 0 

    @classmethod
    def load_config(cls, path="config.yaml"):
        """
        Load a YAML configuration file and return it as a dictionary.

        Args:
            file_path (str): The path to the YAML configuration file.

        Returns:
            Dict[str, Any]: The configuration as a dictionary.
        """

        file_path = Path(path)
        mtime = file_path.stat().st_mtime
        if mtime != cls._last_mtime:
            with open(file_path, "r") as f:
                cls._config = yaml.safe_load(f)
            cls._last_mtime = mtime
        return cls._config
    
    @classmethod
    def get_service_config(cls, service_name: str):
            config = cls.load_config()
            
            services = config.get("services", {})
            models = config.get("models", {})

            service = services.get(service_name)
            if not service:
                raise ValueError(f"Service '{service_name}' not found in configuration.")
            
            model_key = service.get("model")
            model_dict = models.get(model_key)
            if not model_dict:
                raise ValueError(f"Model '{model_key}' not found in configuration.")

            runtime_dict = service.get("runtime", {})

            model_config = ModelConfig(**model_dict)
            runtime_config = RuntimeConfig(**runtime_dict)
            return model_config, runtime_config
