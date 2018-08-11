#!/usr/bin/env sh

# https://developer.oxforddictionaries.com/swagger/spec/public_doc_guest.json
# https://developer.oxforddictionaries.com/swagger/spec/public_doc_registered.json
# https://developer.oxforddictionaries.com/swagger/spec/leap_api.json

swagger-codegen generate \
    -i https://developer.oxforddictionaries.com/swagger/spec/public_doc_registered.json \
    -l python \
    -c swagger.config.json
