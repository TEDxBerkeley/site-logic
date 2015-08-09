#Template Logic Tier

This is a template logic tier for a sample Braiiin application. All application
logic tiers should follow the format specified in this template, unless otherwise
stated.

## Getting Started

Here is how to setup a local instance.

1. Duplicate, not fork, this repository as `[app]-logic`, and clone it.
2. Check that needed commands are accessible `source check.sh`.
3. Install `source install.sh`.
4. Run server `source activate.sh`.
5. Browse [Logic Core Documentation](logic-braiiin.readthedocs.org) if need be.
6. Read the Guidelines below.
7. If you are uncertain of where to start, see "How It Works".

## Guidelines

1. Do not modify the core `logic` submodule, which is located in the `logic`
directory from this repository. If you wish to make edits, clone the `logic`
repository and make edits there.
2. Make all edits in a new branch. After creating a branch, immediately create 
a Pull Request (PR), but include `[do not merge]` in the title, so that your 
teammates can comment and collaborate on the branch.
3. Once the branch is ready, remove `[do not merge]` and alert your code partner
that it is ready for code review.
4. Do not merge your own PRs, unless it is a critical bug fix and all tests pass.
5. Conform to PEP style guidelines.

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

...