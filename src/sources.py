from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class FirebaseSource:
    name: str
    url_env: str
    date_field: str = "fecharaw"
SOURCES: list[FirebaseSource] = [
    FirebaseSource(
        name="production",
        url_env="FIREBASE_URL_PRODUCTION",
        date_field="fecharaw"
    ),
    FirebaseSource(
        name="inputs",
        url_env="FIREBASE_URL_INPUTS",
        date_field="fecharaw"
    )
]