from rich.table import Table

from dataclasses import dataclass


@dataclass
class User:
    """ User type """
    id: int
    name: str
    username: str
    state: str
    avatar_url: str
    web_url: str
    created_at: str
    bio: str
    location: str
    public_email: str
    skype: str
    linkedin: str
    twitter: str
    website_url: str
    organization: str

    def render(self):
        table = Table()

        table.add_row("ID", str(self.id))
        table.add_row("Name", self.name)
        table.add_row("Username", self.username)
        table.add_row("State", self.state)
        table.add_row("Avatar URL", self.avatar_url)
        table.add_row("Web URL", self.web_url)
        table.add_row("Created At", self.created_at)
        table.add_row("Bio", str(self.bio))
        table.add_row("Location", str(self.location))
        table.add_row("Public Email", self.public_email)
        table.add_row("Skype", self.skype)
        table.add_row("LinkedIn", self.linkedin)
        table.add_row("Twitter", self.twitter)
        table.add_row("Website URL", self.website_url)
        table.add_row("Organization", str(self.organization))

        return table
