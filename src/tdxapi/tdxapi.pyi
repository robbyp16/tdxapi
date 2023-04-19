import aiohttp
import requests
from tdxapi import exceptions as exceptions
from typing import Any, Optional

class TeamDynamixInstance:
    no_owner_uid: str
    def __init__(self, domain: str = ..., auth_token: str = ..., sandbox: bool = ..., default_ticket_app_name: str = ..., default_asset_app_name: str = ..., api_session: Optional[aiohttp.ClientSession] = ...) -> None: ...
    def get_id(self, app_name: str, name: str, id_type: Optional[str] = ...) -> str: ...
    def get_default_app_name(self, app_type: str) -> str: ...
    async def close_api_session(self) -> None: ...
    def set_auth_token(self, token: str) -> None: ...
    def get_current_user(self) -> dict[str, Any]: ...
    def get_domain(self) -> str: ...
    def set_domain(self, domain: str) -> None: ...
    async def initialize(self) -> None: ...
    async def populate_ids_for_app(self, app_type: str, app_name: str) -> None: ...
    def load_auth_token(self, filename: str = ...) -> None: ...
    def save_auth_token(self, filename: str = ...) -> None: ...
    async def get_asset(self, asset_id: str, app_name: str = ...) -> dict[str, Any]: ...
    async def search_assets(self, search_string: str, app_name: str = ...) -> list[dict[str, Any]]: ...
    async def update_asset(self, asset: dict[str, Any], app_name: str = ...) -> aiohttp.ClientResponse: ...
    def attach_asset_to_ticket(self, ticket_id: str, asset_id: str, ticket_app_name: str = ...) -> requests.Response: ...
    def search_tickets(self, requester_uid: str, status_names: list[str], title: str, responsible_group_name: str = ..., app_name: str = ...) -> list[dict[str, Any]]: ...
    def get_ticket(self, ticket_id: str, app_name: str = ...) -> dict[str, Any]: ...
    def get_ticket_attribute(self, ticket: dict[str, Any], attr_name: str) -> dict[str, Any]: ...
    def update_ticket_status(self, ticket_id: str, status_name: str, comments: str, app_name: str = ...) -> requests.Response: ...
    def search_people(self, alt_id: str) -> list[dict[str, Any]]: ...
