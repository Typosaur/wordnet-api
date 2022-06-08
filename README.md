# WordNet API

API for WordNet Database made using [fastapi](https://github.com/tiangolo/fastapi)

## Installation

**Note**: You should run the app behind a TLS-terminating proxy like Caddy or Cloudflare, if possible with cache (and high TTL)

### Using Docker

```
docker run -p 80:80 ghcr.io/typosaur/wordnet-api:latest
```

See available environment variables in the configuration section

### From source

1. Install Python 3.6 or above

2. Clone the repository

  ```
  git clone https://github.com/Typosaur/wordnet-api
  ```

3. Install the dependencies

  ```
  pip install --no-cache-dir --upgrade -r app/requirements.txt
  ```

4. Download NLTK data

  ```
  python -m nltk.downloader omw-1.4
  ```

5. Start the uvicorn server

  ```
  uvicorn main:app
  ```

## Configuration

The application is configured by setting following environment variables:

|Variable|Default|Required|
|--------|-------|--------|
|`CORS_ORIGIN`|*|False|

## API

### GET `/synonyms`

#### Query Parameters

|Param|Default|Required|
|-----|-------|--------|
|`word`|None|True|

#### Response Model

```py
class SynonymResponseTerm(BaseModel):
    pos: str
    pos_label: str
    definition: str
    examples: List[str]
    synonyms: List[str]

class SynonymResponse(BaseModel):
    word: str
    terms: List[SynonymResponseTerm]
    license: str
```

Swagger docs are available under `/docs`

## WordNet License

WordNet Release 3.0 This software and database is being provided to you, the LICENSEE, by Princeton University under the following license. By obtaining, using and/or copying this software and database, you agree that you have read, understood, and will comply with these terms and conditions.: Permission to use, copy, modify and distribute this software and database and its documentation for any purpose and without fee or royalty is hereby granted, provided that you agree to comply with the following copyright notice and statements, including the disclaimer, and that the same appear on ALL copies of the software, database and documentation, including modifications that you make for internal use or for distribution. WordNet 3.0 Copyright 2006 by Princeton University. All rights reserved. THIS SOFTWARE AND DATABASE IS PROVIDED "AS IS" AND PRINCETON UNIVERSITY MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, PRINCETON UNIVERSITY MAKES NO REPRESENTATIONS OR WARRANTIES OF MERCHANT- ABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF THE LICENSED SOFTWARE, DATABASE OR DOCUMENTATION WILL NOT INFRINGE ANY THIRD PARTY PATENTS, COPYRIGHTS, TRADEMARKS OR OTHER RIGHTS. The name of Princeton University or Princeton may not be used in advertising or publicity pertaining to distribution of the software and/or database. Title to copyright in this software, database and any associated documentation shall at all times remain with Princeton University and LICENSEE agrees to preserve same.
