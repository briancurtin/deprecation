from deprecation import DeprecatedVariable

no_warning = DeprecatedVariable(
    'no_warning', 'no_warning', deprecated_in="2.0",
    removed_in="3.0", current_version="1.0"
)

just_deprecated = DeprecatedVariable(
    'just_deprecated', 'just_deprecated'
)

details = DeprecatedVariable(
    'details', 'details', **{
        "details": "do something else."
    }
)

shows_deprecated = DeprecatedVariable(
    'shows_deprecated', 'shows_deprecated', **{
        "deprecated_in": "1.0",
        "current_version": "2.0"
    }
)

removed_shows_deprecated = DeprecatedVariable(
    'removed_shows_deprecated',
    'removed_shows_deprecated', **{
        "deprecated_in": "1.0",
        "removed_in": "3.0",
        "current_version": "2.0"
    }
)

shows_unsupported = DeprecatedVariable(
    'shows_unsupported',
    'shows_unsupported', **{
        "deprecated_in": "1.0",
        "removed_in": "2.0",
        "current_version": "2.0"
    }
)

details_shows_unsupported = DeprecatedVariable(
    'details_shows_unsupported',
    'details_shows_unsupported', **{
        "deprecated_in": "1.0",
        "removed_in": "2.0",
        "current_version": "2.0",
        "details": "do something else."
    }
)
