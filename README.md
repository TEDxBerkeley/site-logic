#Template Logic Tier

This is a template logic tier for a sample Braiiin application. All application
logic tiers should follow the format specified in this template, unless otherwise
stated.

## Getting Started

Here is how to setup a local instance.

1. Create a new repository `[app]-logic`, and clone it.
2. Add this repository as a remote named `template` `git remote add template git@github.com:Braiiin/template-logic.git`
3. Fetch `git fetch template`.
4. Merge `git merge template/master`.
2. Check that needed commands are accessible `source check.sh`.
3. Install `source install.sh`.
4. Run server `source activate.sh`.
5. Browse [Logic Core Documentation](http://logic-braiiin.readthedocs.org). (coming soon)
6. Read the [Guidelines](#guidelines) below.
7. If you are uncertain of where to start, see [How to get Working](#how-to-get-working) below.

> To update your installation of the logic core, use:
 1. `git submodule foreach git reset head --hard` to remove any inadvertent changes.
 2. `git submodule foreach git pull origin master` to update the submodules.

## Guidelines

1. It is safer not to modify the core `logic` submodule, which is located in the
`logic` directory from this repository. If you wish to make edits, clone the `logic`
repository and make edits there.
2. Make all edits in a new branch. After creating a branch, immediately create 
a Pull Request (PR), but include `[do not merge]` in the title, so that your 
teammates can comment and collaborate on the branch.
3. Once the branch is ready, remove `[do not merge]` and alert your code partner
that it is ready for code review.
4. Do not merge your own PRs, unless it is a critical bug fix and all tests pass.
5. Conform to PEP style guidelines.
6. Rename the "template" folder in this repository's root to your application's
name.

## How It Works

**High-Level Overview**

The logic core is responsible for accepting, authenticating, and translating
API calls into methods. Each Braiiin logic tier simply treats the core as a
distinct, independent library and registers (1) API endpoints for the application
client to call and (2) models, to define how data is stored.

**Detailed Explanation**

Implementations of the core logic tier only require registered APIs. Assuming
that models are included in the relevant API python files, they will be automatically
detected and registered.

To begin, the `run.py` file, in the repository root directory, creates an instance
of the app, and then runs it. This app is defined in `template/__init__.py`. In
that file, a number of items are necessary for this to function:

1. Updating `sys.path` with the logic directory. This allows your application to
access the logic core as a module named `logic`.
2. In `create_template_app`, it is necessary to import views *after* the app
is instantiated.
3. In `created_template_app`, it is necessary to invoke `app.register_blueprints`
after importing the file that registers your APIs.

In the `template/views.py` file, we import `register_api` and then register
each API with an endpoint name. Note that this file is arbitrarily named. All that
matters, is that this file is imported in `__init__.py` after the app is 
instantiated.

In the `template/api.py` file, you must create API classes that extend from
BaseAPI. Again, this file is arbitrarily named. All that matters, is that an 
imported views file registers this API using the `register_api` method.

##How to get Working

If all of the above is confusing, then simply respect the application's
abstractions and know the following. These should compartmentalize the
application enough, so that you don't need to know how the rest of it works.

1. Create an API in `api.py` that extends from `BaseAPI`.
2. Register the API by calling `register_api` with it, in `views.py`.
3. Read through the sample `SampleAPI` and remove it.
4. Learn how to use models. These are all 
[mongoengine documents](http://mongoengine.readthedocs.org/en/latest/apireference.html#documents)
but you can also use a set of [simpler abstractions](https://github.com/Braiiin/logic/blob/master/logic/v1/models.py).
All models extend that Document object, so refer to the specified examples for
usage.
5. Write tests.