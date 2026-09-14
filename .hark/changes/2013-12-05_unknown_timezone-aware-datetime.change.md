---
title: Timezone aware `datetime` objects passed to the API will now be encoded in a way that does not depend on the local system time.  If you are passing timezone-aware datetimes to our API and your server time is not already in UTC, this will change the value passed to our API.
section: Backwards incompatible changes
released_in_version: 1.11.0
---
