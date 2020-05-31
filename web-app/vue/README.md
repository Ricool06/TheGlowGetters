Light Graph
===========

[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)][license]
[![](https://img.shields.io/badge/Author-The%20Glow%20Getters-ff69b4.svg)](https://twitter.com/TheGlowGetters)

This repository contains the source code for [`light-graph`][light-graph] which
was developed for the [Space Apps COVID-19
Challenge](https://covid19.spaceappschallenge.org/). Many countries around the
word have established restrictions on movement in response the COVID-19
pandemic. Using night light data [`light-graph`][light-graph] monitors networks
of movement, towards understand the effectivness of mesaures used to slow
the speard of the virus and to understand for the future how based to disrupt
the virus accross these graphs.

Development
-----------

For every new task that requires additional commentary or will produce resources
like new figures you should first create a [new issue][new-issue] to track it's
progress.

If there are resources associated with this issue (such as figures or data
files) create a new subfolder in the folder `/issues` after having
[created the issue][new-issue] on GitHub. For example
`/issues/5-some-time-domain-plot`. Make sure to include the issue number at the
beginning of the folder name. Optionally add a short dash case qualifier tag to
the end to make it quick and easy for others to know what the resources are for.

When you commit resources make sure to include `#<issue-number>` at the end of
the first line of your commit message. This will then associated that commit
with the issue, it will show up in the history of the issue making it easier
to find resources and help when reading through the commit history. For example
`Add new figure #5`.

License
-------

[`light-graph`][light-graph] is released under the [MIT license][license].

[light-graph]: https://github.com/Ricool06/light-graph
[license]: LICENSE.md
[new-issue]: https://github.com/Ricool06/light-graph/issues
