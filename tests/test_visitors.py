"""Tests for the Bird Buddy recent-visitors tracker."""

from unittest.mock import MagicMock

from birdbuddy.feeder import Feeder

from custom_components.birdbuddy.visitors import RecentVisitors


def _visitors(hass):
    feeder = Feeder({"id": "feeder1", "name": "Bird Buddy"})
    return RecentVisitors(feeder, MagicMock(), hass)


async def test_on_new_postcard_sets_latest(hass):
    """_on_new_postcard rebuilds media and species from the slim payload."""
    visitors = _visitors(hass)
    event = MagicMock()
    event.data = {
        "postcard_id": "pc1",
        "feeder_id": "feeder1",
        "species": [{"id": "s1", "name": "American Robin"}],
        "media": {
            "__typename": "MediaImage",
            "contentUrl": "https://example.invalid/c.jpg",
            "thumbnailUrl": "https://example.invalid/t.jpg",
            "createdAt": "2026-07-09T12:00:00.000+0000",
        },
    }
    await visitors._on_new_postcard(event)

    assert visitors.latest_species is not None
    assert visitors.latest_species.name == "American Robin"
    assert visitors.latest_media is not None
    assert visitors.latest_media.content_url == "https://example.invalid/c.jpg"


async def test_on_new_postcard_without_data_is_ignored(hass):
    """A postcard with neither media nor species leaves the state unset."""
    visitors = _visitors(hass)
    event = MagicMock()
    event.data = {
        "postcard_id": "pc1",
        "feeder_id": "feeder1",
        "species": [],
        "media": None,
    }
    await visitors._on_new_postcard(event)

    assert visitors.latest_media is None
    assert visitors.latest_species is None
