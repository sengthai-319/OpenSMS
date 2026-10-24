# App Details

## Changes

### Unreleased
- Rebranded to **CrossHubSMS**: new name, logo, app icons and theme colors
- New Android app ID `io.github.sengthai319.crosshubsms` (installs as a separate app from OpenSMS; settings and API keys start fresh)
- New API keys use the `chsms_` prefix
- iPhone support through a Mac: on macOS, SMS are sent through the Messages app and delivered by the paired iPhone (Text Message Forwarding)
- macOS app data is now stored in `~/Library/Application Support/crosshubsms`

### 0.1.1
- Fixing app crash on some mobile GPU with kivymd 2.x . Thanks to [DorDeorz](https://github.com/DorDeorz) for the fix in [UniversalDownlaoder](https://github.com/DorDeorz/UniversalDownloader).

### 0.1.0
- App will check if required permissions are granted
- Adding logging for API requests
- Fixing the android bottom padding
- Adding a back button

### 0.0.1
- Initial version
