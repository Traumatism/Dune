import requests

from ..common.types.user import User
from ..common.base import DuneModule

UIDS = list(range(10))


class UserEnum(DuneModule):
    name = "user-enum"
    description = "to enumerate Gitlab users"

    def run(self) -> None:
        self.add_headers("Host", self.host)
        self.add_headers("Accept", "application/json, text/plain, */*")
        self.add_headers("Referer", self.target)

        for uid in UIDS:

            with requests.get(
                self.target + f"/api/v4/users/{uid}",
                headers=self.headers,
                verify=False
            ) as response:

                if response.status_code != 200:
                    continue

                json_response = response.json()

                user = User(
                    id=json_response["id"],
                    name=json_response["name"],
                    username=json_response["username"],
                    state=json_response["state"],
                    avatar_url=json_response["avatar_url"],
                    web_url=json_response["web_url"],
                    created_at=json_response["created_at"],
                    bio=json_response["bio"],
                    location=json_response["location"],
                    public_email=json_response["public_email"],
                    skype=json_response["skype"],
                    linkedin=json_response["linkedin"],
                    twitter=json_response["twitter"],
                    website_url=json_response["website_url"],
                    organization=json_response["organization"]
                )

                self.console.log(user.render())
