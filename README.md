Hello again, this is a tool that decrypts and obtains CDMs activation authorization keys, Or in other words, it breaks the protection of media players by generating activation keys instead of obtaining Widevine license.

What is CDMs ?
Widevine Content Decryption Modules (CDMs) are how streaming services protect content using HTML5 video to web browsers without relying on an NPAPI plugin like Flash or Silverlight.
For more info about this concept : https://ottverse.com/eme-cenc-cdm-aes-keys-drm-digital-rights-management/

This idea is considered open source, but I created a tool for it to make it easier and save time because the topic is almost complicated.
The tool is built entirely on the Python language and its operation requires some extensions.

Required extensions:
  colorama
  requests
  bs4
  json

You must ensure the presence of these extensions before using the tool to avoid any errors.

API Provider : https://cdrm-project.com/