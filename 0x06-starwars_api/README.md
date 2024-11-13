# 0x06. Star Wars API

## Overview

This project, **Star Wars API**, is designed to interact with the Star Wars API and retrieve character information based on a specified movie ID. The objective is to fetch all character names from a given Star Wars movie and display them in a sequential list. This project reinforces skills in JavaScript, API interaction, asynchronous programming, and command-line arguments in Node.js.

## Concepts

To successfully implement this project, the following concepts are essential:

- **HTTP Requests in JavaScript**:
  - Making HTTP requests to external services using the `request` module.
  - Alternatives such as `fetch` for retrieving API data in Node.js.
  - [A Complete Guide to Making HTTP Requests in Node.js](https://www.memberstack.com/blog/node-http-request)

- **Working with APIs**:
  - Understanding RESTful APIs and parsing JSON data.
  - Sending HTTP requests and managing response data.
  - [Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)

- **Asynchronous Programming**:
  - Handling asynchronous operations with callbacks, promises, and async/await.
  - Asynchronous data handling for displaying API response data.
  - [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)

- **Command Line Arguments in Node.js**:
  - Accessing command-line arguments in Node.js with `process.argv`.
  - Parsing command-line arguments for dynamic API requests.
  - [How to Parse Command Line Arguments in Node.js](https://tecadmin.net/how-to-parse-command-line-arguments-in-nodejs/)

- **Array Manipulation and Iteration**:
  - Iterating over arrays and handling data structures to format and display Star Wars character names.
  - [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

## Project Requirements

- **Environment**:
  - All files will be interpreted on **Ubuntu 20.04 LTS** using **Node.js (version 10.14.x)**.
  - Code should adhere to the **semi-standard** code style (rules of Standard + semicolons) with reference to AirBnB style.

- **File Setup**:
  - The first line of each file should be `#!/usr/bin/node`.
  - All files should end with a new line.
  - All files must be executable.
  - No use of `var` is allowed.

- **Required Modules**:
  - Install `request` module for API requests:
    ```bash
    sudo npm install request --global
    export NODE_PATH=/usr/lib/node_modules
    ```
  - Install `semistandard` for code style compliance:
    ```bash
    sudo npm install semistandard --global
    ```

## Tasks

| Task No | Filename                      | Description                                                                                                   |
|---------|--------------------------------|---------------------------------------------------------------------------------------------------------------|
| 0       | [0-starwars_characters.js](./0-starwars_characters.js) | A script that fetches and prints all characters of a specified Star Wars movie, based on the movie ID provided as an argument. |

### Task Details

#### 0. Star Wars Characters

**Filename**: `0-starwars_characters.js`

- **Objective**: Write a script that takes a **Movie ID** as the first positional argument and fetches character names from the specified Star Wars movie.
- **API Used**: The [Star Wars API](https://swapi.dev/documentation), specifically the `/films` endpoint.
- **Expected Output**: Each character's name from the movie appears on a new line, in the order they are listed in the "characters" array in the API's response.

**Example Usage**:
```bash
./0-starwars_characters.js 3
```

**Example Output:**
```
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
...
```
