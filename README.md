# The Big Webservice

### A Fun Coding Exercise

Hello fellow developer! I have completed this webservice according to a number of requirements
handed to me by my business people. I'd like you to take a look at it and send me a pull request
of everything you would change to make it production ready! This might include things like
changing program composition, adding extra files, cleaning up my source code... you know, the
good stuff. Heck, I don't even know if the REST API I made is perfect - that's on the table for
review as well.

I'd do the work myself however there are ants in my house that require my full and undivided
attention to defeat.

Good luck!

### Getting Points

Fixes to the codebase are graded on their importance via the table below. Solved issues that
are higher up on the table are worth more points. When you submit your pull request you must
have a list of fixes made to the codebase in your pull request. In addition, you should
understand your fixes enough to speak to the hows and whys of each change.

**Changes to the API are encouraged and are graded under design and composition!**

<table>
    <tr>
        <td>Logic and Validation Errors</td>
        <td>+4</td>
    </tr>
    <tr>
        <td>Desgin and Composition</td>
        <td>+3</td>
    </tr>
    <tr>
        <td>Best Practice Conformance</td>
        <td>+2</td>
    </tr>
    <tr>
        <td>Syntax Lint</td>
        <td>+1</td>
    </tr>
</table>


### Running TBWS
```bash
pip install -r tools/pip-requires
pip install -r tools/test-requires
gunicorn tbws.service:app
```

### TBWS Requirements

* Must be able to store and retrieve key-value pairs
* Must be able to return the largest value stored

### TBWS API

#### /things/put/{key}
**Methods: POST, PUT**  
**Content-Type: application/text**

Puts the content body of the request into the DB under the key URI parameter.

#### /things/get/{key}
**Methods: GET**  
**Content-Type: application/text**

Gets the value stored in the DB under the key URI parameter.

#### /things/get_largest
**Methods: GET**  
**Content-Type: application/text**

Gets the largest value stored in the DB.
