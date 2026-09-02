from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App
    app_name: str = "School Timetable"
    debug: bool = False

    # Database
    database_url: str = "sqlite:///./data/output/school_timetable.db"

    # Solver
    solver_time_limit_seconds: int = 30
    solver_num_workers: int = 8

    # Soft constraint weights (penalizaciones por defecto)
    weight_teacher_gap: int = 1
    weight_teacher_preference: int = 2
    weight_room_change: int = 1

    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_")


settings = Settings()