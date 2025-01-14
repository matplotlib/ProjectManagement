# Matplotlib Weekly Meeting 

**A regular sync meeting for the project's maintainers, which is open to the community.** Everyone is welcome to attend and contribute to conversations.

## February 22 2024 - Jan 09 2025


###### tags: `2024 dev call`


Call co-ordinates:  Thursdays @ 21:00 Berlin time (20:00 UTC during winter, 19:00 UTC during summer) https://zoom.us/j/384435716?pwd=WFpxVWxoYXArTDFzN1lWaHNoOE8xZz09

Previous notes: [Meeting Agendas](https://hackmd.io/zljR-pZrQ0O5J_j4NZ-9yw)
Archive: [matplotlib/ProjectManagement](https://github.com/matplotlib/ProjectManagement)

#### [Needs discussion at some point](https://hackmd.io/uzWviu8zSUChq3XhI2FqPg)

#### [Medium sized projects](https://hackmd.io/GgtrcXTlTfuoyHO76_LMLg)

#### [RSE worklog](https://hackmd.io/@matplotlib/HyVoUHlSo)

```
2023-04-20 19:00:00+00:00
Europe/Berlin        2023-04-06 21:00:00+02:00
UTC                  2023-04-06 19:00:00+00:00
America/New_York     2023-04-06 15:00:00-04:00
America/Vancouver    2023-04-06 12:00:00-07:00
US/Hawaii            2023-04-06 09:00:00-10:00
```

# Jan 9
_attending_: @greglucas, @efiring, @story645, @tacaswell, @rcomer, @ksunden, [@efiring](@QWhXj01mSwmTjk5kN1H_qQ) 

## Agenda
### old business
- [x] 3.10 doc tweaks
- [x] NASA updates
- [x] RSE updates

### new business

## Notes

### RSE updates
- Tom
    - time off
    - python-build-standalone 
        - https://github.com/astral-sh/uv/issues/6893#issuecomment-2565965851
    - some review
- Kyle
    - some time off
    - working on planning the next 2 months of work
    - catch up

### what big stuff is in the pipe?
 - bivariate colormap (has PR, needs review)
 - bezier work (from Bruno)
 - PR to vectorize 3D code 
     - some have been resurected by Scott
 - font work! (raq)
 - groupbar chart
 - what artists get a label attribute
 - start to look at ticks


### [labels](https://github.com/matplotlib/matplotlib/issues/29422)
 - to ideas:
     - want to have a unique id so you can select artist by name [2](https://github.com/matplotlib/matplotlib/issues/29429)
         - sometimes people (ab)used the label API for this
     - label is top-level artist property to be used in legends even on things that should never be in the legend (like the Legend itself or the whole figure)


# Dec 26
_attending_: @efiring, @tacaswell, @story645 

# old business


## notes
- request to prioritize Remote Frame Buffer

# Dec 19 
_attending_: @story645, @ksunden, @QuLogic 

### Old business
- [ ] RSE updates
### New business

## Notes
- Kyle : 3.10 release
- Elliott : font internationalization


### [edge/hatch color](https://github.com/matplotlib/matplotlib/pull/28104)
- is edge intended as a color spec? 'inherit' can be passed in through color or rcParam
- should transparent edgecolor be special cased when hatch is set and no hatchcolor is set

# Dec 12
_attending_: @story645, @greglucas, @ksunden, @tacaswell, @QuLogic 
## Agenda
### Old business
- [ ] RSE updates
### New business
- [x] 3.10
- [x] Data symlinks in wheels not working ([Issue](https://github.com/matplotlib/matplotlib/issues/29229))
## Notes
### missing files
- determined that the missing files is due to a change in meson-python between 0.16.0 and 0.17.0
- will pin back and quickly cut a 3.9.4
- will tag 3.10.0 as soon as this is done

### RSE updates
 - Tom
     - not much, busy with other resonsibilities
 - Kyle
     - trying to sort out a series of "one more thing..." for 3.10
 - Elliott
     - trying to get back on top of reviews
     - work on font stuff
         - couple of nice-to-have before pulling bulk of raqm work in
         - type3 fonts in pdf can be nicer
             - characters out of ascii plane are rendered in the right place but as "xobject" not as text so highlighting is super broken
             - may be able to use a very custom code page that supports the first 256 glyphs as proper text
         - do we care about type3
             - its complicated
             - publishers may still care
         - maybe able to get ghostscript to do type1 -> type3 conversion

# Dec 5 
_attending_: @QuLogic, @ksunden, @story645, @NGWi

## Agenda
### Old business
- [x] RSE updates

### New business
- [x] 3.10

### Notes
- [xkcd](https://github.com/matplotlib/matplotlib/issues/29233)
    - probably just an error on local fonts
- [transparent animation](https://github.com/matplotlib/matplotlib/pull/29024)
 - Was reported as not a functioning fix in a comment on the PR 
 - can't reproduce  

# November 21
_attending_: @tacaswell @efiring @ksunden @qulogic @story645 

## Agenda
### Old business
- [ ] RSE updates

### New business
- [ ] 3.10


## Notes
### RSE updates
 - Kyle
     - 3.10 finalizing PRs had more back-and-forth than expected
         - vert deprecation [#29155](https://github.com/matplotlib/matplotlib/pull/29155)
             - switch deprecation to "pending"
             - this will still fail pandas (because they have opted it to more warnings)
             - we will PR to fix pandas
         - converter relaxation [#29154](https://github.com/matplotlib/matplotlib/pull/29154)
             - merged to main
             - PR to 3.10.x pending
 - Elliott
     - gtk snapshot work, issues with fractional high-dpi
     - CI audit: https://gist.github.com/QuLogic/1ef085d97e1f29d29045455411d686e9
         - action: try dropping azure linux + macOS
             - reduce power usage, reduce total build time
     - discussion of flaky tests on windows
         - mostly seems connected to subprocess
- Tom
    - some review, work on LLM rules


### test determinism test 
 - ghostscript does not promise determinism of output, so we can not test for it!
 - consider removing test (or atleast ps part)
- stalled PR from @oscargus to remove distillation may be related

### LLM chat

 - https://github.com/matplotlib/matplotlib/pull/28335

# November 14
_attending_: @tacaswell @greglucas  @ksunden @QWhXj01mSwmTjk5kN1H_qQ 

## Agenda
### Old business
- [x] RSE updates

### New business
- [x] 3.10.0rc1 fallout?


## Notes
### RSE updates
 - Kyle
     - data prototype work
         - thinking about collections
     - incompatibility with tcl9, working on finishing PR
 - Elliott
     - finished wasm work
         - PRs will run
         - still evaluating canvas backend, maybe platfrom specifc dependencies for wasm builds
     - gtk4 modernization
         - direct buffer copy vs cairo
     - finished rebuild of fedora
         - 10 packages failed to rebuild, some already fixed by upstream (out of 150 odd)
         - some were ignoring deprecations
         - no seaborn-scale downstream broke
         - builds: https://copr.fedorainfracloud.org/coprs/qulogic/matplotlib-310/packages/
         - checks: https://copr.fedorainfracloud.org/coprs/qulogic/matplotlib-310.checker/packages/
             - anything that fails in the first link, but _doesn't_ in the second is a new failure
             - APLpy - actually failing in astropy; [fixed upstream](https://github.com/astropy/astropy/pull/17145)
             - gdl - flaky test, not a real failure
             - morphio - pybind11, not us; [fix available upstream](https://github.com/BlueBrain/MorphIO/pull/508)
             - myst-nb - tests are [version-specific](https://github.com/executablebooks/MyST-NB/blob/master/pyproject.toml#L98-L99), but unlikely to be fully broken
             - python-animatplot - [fixed upstream](https://github.com/boutproject/animatplot-ng/pull/25)
             - python-fsleyes-widgets
             - python-mplcairo - fixed in 0.6
             - python-pandas - axis converter warning, and deprecation of `vert` argument to `boxplot`; @ksunden to investigate
             - python-plotnine - deprecation warning caught by tests, but it's [fixed upstream](https://github.com/has2k1/plotnine/commit/6cc67c156cc3f9aa2d85f13aea06bc7abee7eaac#diff-11be2f3ae9ad00a253129ee11716189ca7175d027da3618274f690503a28d19aL786), not packaged yet
 - Thomas
     - behind the scenes NASA grant
     - bit of review and discussion with Kyle

### 3.10.0 final

Target this Friday

### Timers
 - PR: https://github.com/matplotlib/matplotlib/pull/29062
 - What do we want to do for accuracy of timers on CI systems?
     - CI systems are troublesome with their timers. All tests pass locally.
     - Keep the current PR as-is and target 3.11, nothing urgent for 3.10.
     - Try to make longer tests with longer iterations to avoid issues with slow CI systems. (long running tests are currently ~25s)
         - Make sure to change time based on local vs CI
 - 


# November 7
_attending_: @tacaswell, @efiring, @ksunden, @story645, @QuLogic 
## Agenda
### Old business
 - [x] RSE updates

### New business
 - [x] 3.10rc1 fallout?
 - [ ] sprint report

## Notes
### RSE updates
- Kyle
    - rc 3.10 out (technically in October)
    - trying to focus on data-prototype work
- Tom
    - grant work
    - pydata NYC sprints
    - bits of review/contributions
- Elliott
    - 3.10rc1 testing (fedora build to futher build down stream)
    - Work on wasm build
        - need to skip subprocess / thread tests
        - they have a canvas backend that we might adopt
        - how does this intersect with jupyterlite?
            - we think they are using the canvas backend, need to talk to them
        - need to look into how to get nightly wheels for pyodide available if we want to use jupyterlite for our docs
        - we do have some cut-outs because we fully control our own server and can host what ever we need to
        - might need to tune "how to clean old wheels" script (shared problem)


### rc1 fallout
- none yet!

### sprint report

- got a few first-time contributors through

# October 31
_attending_: @tacaswell, @QWhXj01mSwmTjk5kN1H_qQ, @QuLogic ,@ksunden, @story645 , @timhoffm 
## Agenda
### Old business
 - [x] RSE updates
 - [x] 3.10 status update
### New business
 - [x] NF CoC


## Notes
### CoC

#### Conetxt 

Email from NF

> Dear Projects, 
>
>
>
>We are happy to announce that the NumFOCUS Board of Directors approved the new NumFOCUS Code of Conduct on Sept. 4, 2024. Before the Code of Conduct can be implemented, the NumFOCUS Code of Conduct Working Group must be established and receive training. We plan to complete this process by the end of January 2025.
>
>
>
>Current: NumFOCUS Sponsored and Affiliated projects can opt-in to use the new Code of Conduct. Starting Feb. 1, 2025, all new NumFOCUS projects will be asked to opt-out of using the NumFOCUS CoC. NumFOCUS events, including PyData, will continue under the NumFOCUS Code of Conduct in place.
>
>
>
>NumFOCUS Code of Conduct Working Group Election
>
>We are looking for individuals willing to serve in the Working Group that will be tasked with reviewing, investigating, responding to, and advising on potential conduct violations and advising a broad NumFOCUS ecosystem member on the NumFOCUS Code of Conduct. The term is one year. Please find more information, as well as the nomination form, in this blog post.
>
>
>
>Your Decision Process 
>
>For your project currently with NumFOCUS, the new CoC is opt-in. To support your project in making an informed decision, as well as help in the potential implementation, we are planning the following actions:
>
> 1. Jan. 2025: Walk-through video + email + meetings for the Projects and PyData chapters
> 2. Feb. 2025: Current Projects’ decisions to opt-in are captured via a Typeform submission
> 3. Mar. 2025: Meeting with Project adopters to provide materials:
>    - Welcome pack:
>       - pre-drafted text that you can put on your website / GitHub README file
>       - a link to our CoC information, which will include the reporting button
infographic of the reporting procedures
>     - Education:
>        - online materials covering CoC-related best practice
>
>
>Please let us know if you have any questions. Feel free to contact Kamila Stepniowska (Project DEI Lead) by email (kamila@numfocus.org) or via Slack.
>
>
>
>Thank you,
>
>Arliss

NF CoC: https://numfocus.org/2025-code-of-conduct
Our current CoC: https://matplotlib.org/stable/project/code_of_conduct.html

Currently we use Contributor Covenent 2.0 verbatim, NF CoC is new text synthesised from a number of existing CoC including Contributor Covenent 1.4 

Looks like we can not make a decision until Feb 25 and there will be more information / materials available to us in Jan 25

#### Discussion 

Consensus is we are still interested.

### RSE updates
 - Kyle
     - work on 3.10
     - rc1 TODAY
 - Elliott
    - sick this week
    - got thourgh animation work
        - all codecs could find work
    - polar PR position in layouts
    - starting to look at alt-text
    - CI audit
        - mostly done, still in progress sorting out where we skip which tests
            - mostly GUI toolkits
        - appveyor is the only one that runs with conda
        - azure is a multidue of windows
        - azure vs GHA have slightly different osx runners
        - freethreading only on GHA
- Tom
    - 3.10 work
    - grant prep work

### 3.10
- 3 PRs
    - https://github.com/matplotlib/matplotlib/pull/28048
        - merged, docs failures we think will work when meregd 
    - 


### sprint prep

- https://github.com/matplotlib/matplotlib/issues/28920
- target switch to `!` to supress broken links as a sprint activity (#28290)
- @story645 will take a pass at turning this into a usable task-list for the sprint at pydata NYC next week
  - will edit into original issue

# October 24
## Agenda

### Old business
- [x] RSE updates
- [ ] 3.10 progress
### New business

- [x] ROSES 2024
    - https://www.nasa.gov/news-release/nasa-funds-open-source-software-underpinning-scientific-innovation/ We were selected for a 5 year grant to support mpl + cartopy

## notes

### RSE updates
- Tom
    - behind the scenes paperwork for NASA grant
    - some review
- Kyle:
    - macos input hook issues
    - 3.10 work
- Elliott
    - 3.10 things
    - finished polar work (needs to be commited and PRd)
    - looking at transparent animation
        - ham-fisted compositing to white not great (Caswell added that)
        - adding cut-out for more formats that support it
    - need website reviewed to turn of pluto
        - Done!

### 3.10


# October 17
_attending_:@efiring, @ksunden, @QuLogic,


## agenda
### old business
- [ ] RSE

## Notes

### 3.10

- MacOS CI problem solved, but needs a backport.
- Color pipeline: needs another rebase (Kyle).
- Nothing else is blocking; a few more might get in.
- goal: branch tomorrow or Monday
- merge reference cycle fix? https://github.com/matplotlib/matplotlib/pull/28861

### 3.9.3
- worth doing
- some backports
- https://github.com/matplotlib/matplotlib/pull/28981


# October 10

_attending_:@efiring, @ksunden, @QuLogic, @greglucas, @tacaswell, @story645 

## agenda
### old business
- [ ] RSE
- [ ] [name=hannah][NumFocus CoC](https://numfocus.org/2025-code-of-conduct)


## Notes

### COC
- NF has released text, discuss in 3 weeks

### 3.10
- 3D PR is almost done
- push hatch/edge color API cleanup to 3.11
- go ahead with colorizer PR
- ttconv pr
    - https://github.com/matplotlib/matplotlib/pull/20866
    - https://github.com/matplotlib/matplotlib/pull/28784 for example of type42
- long discussion of thread/freethreading

### RSE update
- Elliott:
    - progress on website redirects
        - now have proper 301 redirects instead of symlinks
        - https://github.com/matplotlib/matplotlib.org/pull/41
        - running on https://pluto.matplotlib.org
    - yesterday looked like we were getting hammered by AI bot
        - turned on cloudflare cdn for discourse
        - followed guide on how to do this, but report issues
    - enable bot-protection on CF, this broke inventory downloading for inter-sphinx, turned off

# October 3
_attending_: @ksunden, @QuLogic, @efiring

Informal meeting with some discussion of PRs for 3.10.

3-D rotation PR: needs a decision, or delay to 3.11.

3.8 deprecation removals

https://github.com/matplotlib/matplotlib/pull/28658: Tim?

# September 26th
_attending_: @ksunden, @QuLogic, @efiring, @story645, @timhoffm 

## Agenda
### old buisness
- [ ] RSE

### new business
- [x] [name=hannah] hacktoberfest?

## Notes

### hacktoberfest 
- Evaluation is neutral; hard to evaluate long-term value.  There is some willingness, but no enthusiasm.
    - we're too under-resourced at the moment 
- take out topic
- they can request a `hacktoberfest-accepeted` tag

### [removal of `cbook.Stack`](https://github.com/matplotlib/matplotlib/pull/28874)
- this was deprecated in 3.8, and the linked PR removes it for 3.10
- however, there exists a usage of it in the type stubs for `lib/matplotlib/backend_tools.pyi:ToolViewsPositions` (but is not otherwise documented)
- for now, we will fix mypy by keeping the private `cbook._Stack` in the type stubs
- can open a followup issue or PR to deprecate the `ToolViewsPositions` internals if wanted

### [fixed aspect overwrites explicitly set data limits](https://github.com/matplotlib/matplotlib/pull/28683)
- accept the pr

### [fontproperities init](https://github.com/matplotlib/matplotlib/pull/28843)
- distinguishing if string is family or pattern
- alternative proposal/concern is that someone may have passed in a pattern as a family kwarg arg - undocumented but supported use case
    - we can let that work for the time being and worry about it later 
        - can't warn b/c of lack of distinction between names and patterns 
            - we can check if a string is a pattern b.c we can run it through the machine
            - can't determine if it's a family name
    - we want to ask `not family` but we can't get the full set of families
- merged
- follow up: either leave it or figure out pattern|family or restrict names

### 3.10 queue
- colorizer
- pybind11



# September  19th


## Agenda
_attending_: @tacaswell, @ksunden, @QuLogic, @efiring, @story645 

### old business
- [x] RSE

### new business
- [ ] [name=@story645] github teams for non-code work:
    -  survey: Jerome (@jeromefv-former GSOD) and Tammy (@tgmiller5)
        -  survey repository (also backup old survey here)
    -  social: Pawel (@pawjast) -> social media projects board
- [ ] 3.10 status / burndown
- [x] [name=greglucas] Potential funding through OpenTeams [REPOS project](https://www.openteams.com/introducing-repos-platform-for-sustainable-open-source-funding/)
    - Propose bugs to squash or improvements to make and companies can pay developers to work on those specific items because it may be blocking them

### issues and PRs

## Notes
### RSE updates
 - Tom
     - issue triage and review
     - meeting with Kyle/Elliott
 - Kyle
     - issue / PR triage
     - aiming for 3.10 rc next week
     - implementing a setter for converters on `axis` objects for 3.10
     - data prototype work
 - Elliott
     - triage work
     - pybind11 and ft2font work
     - close to PR to remove our numpy wrapper (and only use pybind11's)
     - working on sizing polar plots correctly
     
### REPOS project

- we propose specific projects with budgets
- companies fund said projects
- run through openteams
- follow up again when Greg is on the call

#### github teams/ recognition of non-code contributions
- create a repo for the survey
- add teams for survey and social media
- Numpy web page "teams" example https://numpy.org/teams/ (generated from Github teams)

# September 12th

## Agenda

_attending_ : @tacaswell @timhoffm @story645 @IGuKs80UTJCig4yt6Zos7w (greglucas) @ksunden @trygve @QWhXj01mSwmTjk5kN1H_qQ (efiring) @rcomer 

### old business
- [x] RSE
- [x] [name=@story645]user survey - do we have an mpl google account for forms? 
    - who should own it?
    - [very rough draft of questions](https://hackmd.io/3xLJ88NhQrG_BOXrWKGp1Q#List-of-questions-and-available-responses)

### New business
- [x] [name=@greglucas] NumFOCUS Summit updates
    - [ ] NetworkX requests
        - Bezier path improvements and distance along curve
        - Arrow to the edge of a marker (Greg: Is there a way to update this with the transform stack and `get_tightbbox()`? I'd be worried about interactively moving a marker and getting the arrow to follow)
- [x] [name=@greglucas] Squash merging rather than asking new contributors to squash themselves
- [x] pybind11 updates
- [ ] mpl 3.10 updates
    - https://hackmd.io/l9vkn_T4RSmk147H_ZPPBA?both#310
    - PR for [grouped bar charts](https://github.com/matplotlib/matplotlib/pull/28560) [Tim] -> API feedback welcome
- [ ] arrows are hard
- [x] opt into NF CoC scheme 

## Notes
### NF summit
 - news: Leah is stepping down
 - discussions about
     - web assembly
     - SDG program
         - NF "developer-in-residince" to spread across projects
     - SPEC process
     - updates for Python freethreading
         - lots openMP thread
     - https://github.com/numfocus/project-summit-2024-unconference/issues for more details
 - CoC updates
    - Opt-in for current projects
    - Opt-out for new projects coming in
    - NumFOCUS Code of Conduct Working Group (coming soon)
    - Code of Conduct Event Response Teams (organizers create for a particular event)
    - coming soon
- cross-project development
    - discussion with networkX
    - revival of some old PRs from Bruno about Bezier curves
    - enhancements around pointing arrows to edges of other paths
    - (discussion of arrows and why they are)
    
### CoC opt-in

- high level discussion sound good
- early drafts had same pro/con as our current process
- Caswell in in favor to get benifit of a bigger pool
- wait for actual details before committing

### RSE updates
 - Kyle
     - summit most of last week
     - data prototype work on patches
     - issue / PR review
 - Elliott
     - mostly pybind11 work
     - rebased ttfconf PR that switches to using fonttools
         - also fixes a bug we only just discovered with font subsetting
 - Tom
     - project management
     - little bit of review

### user survey 
- please contact NF for getting access to a form
- there exists a rough draft of questions
    - justification of questions still in process
- aiming for early to mid fall to be ready

### squash merge
- do we want to just squash-merge?
- vote to (socially) prefer squash merge

### pybind11
- just needs review effort
- still left after these:
    - macosx (not c++ so leave)
    - some internal stuff that is waiting on these PRs
    
### mpl 3.10

- can we just cut from main now?
  - colorbar stuff
  - colorizer can be merged
    - what is left on colorizer?
        - currently doing last round of review
        - @timhoffm hoffm should take another look
        - consider if there is a better way to fix `isinstance`
- have a proposal for group bar charts from @timhoffm 
    - everything is marked as provisional [#28560](https://github.com/matplotlib/matplotlib/pull/28560)
- @ksunden will be release manager, we need to update the goverance docs
    - updated docs: https://github.com/matplotlib/governance/pull/41
- pybind11 in for 3.10 (yes)
- freethreading?
    - qhull is probably ok
    - contourpy claims in is safe
    - kiwi is a question
    - freetype in theoritically safe
        - ft2font has no locks
        - agg may lock the font cache
    - plan
        - build 313t wheels
        - option 1: do not mark as safe
            - document that we need users to test with the force free-thread env
            - this may be closer to what CPython does
        - option 2: mark as safe
            - numpy has marked them selves safe
            - using a freethreading build is opting into segfaults 
        - fliping on/off in a mirco seems ok
        - 

# September 5th
_attending_ : @efiring, @story645, @QuLogic 
## Agenda

### Old business
- [ ] RSE


## Notes
### RSE
- Kyle @ summit 
- Elliot still needs SDG paperwork, has been working primarily on FT2Font work
- Question about license in [font test](https://matplotlib.org/devdocs/project/license.html#fonts)
    -no specific license file for Dejavu
### pydata nyc
- finish out tagging PRs bf sprints
    - https://github.com/matplotlib/matplotlib/pulls?q=is%3Aopen+is%3Apr+label%3A%22Documentation%3A+tags%22



# Aug 29th
_attending_ : @greglucas, @efiring, @ksunden, @QuLogic, @story645, 

## Agenda

### Old business
- [x] RSE
- [x] GSOC
    - [x] how to manage documentation of colorizer

### New business
- [x] link exceptions in docs
- [x] [fig.annotate](https://github.com/matplotlib/matplotlib/pull/28753)

## Notes
### RSE
 - Kyle
    - some time on getting NF summit travel sorted
    - wrapped up GSOC evalution
    - working on data prototype `Patches`
    - PR review
- Tom
    - Review
    - fixing the docs on the colorizer PR
- Elliott
    - mostly ft2font, many test cases
    - found a few bugs
    - useful to validate the planned pybind11 work
    - paper work for SDG, plan to start work next week


### GSOC
 - is over. final report: https://trygvrad.github.io/gsoc-2024-bivariate-colormaps-summary/
 - some was merged, not everything we planned
 - we drove a change-of-scope that changed goals
 - potentially fix docs w/ a script (called from conf.py) that writes out the .rst from *_scalarmappable* and is then included in write place via .. include::

### doc links:
- have sphinx document private methods by default -> sphinx allows manual over ride
    - make these public abstract methods
- to handle methods on subclasses 
    - https://github.com/sphinx-doc/sphinx/issues/11434
- can curate which methods are included/excluded by excluding specifc parent classes
- with collection: document private with sizes for now

# Aug 22nd
_attending_: @greglucas, @efiring, @ksunden, @QuLogic, @story645, @trygvrad, @tacaswell, @litchi

### Old business
- [x] RSE
- [x] GSOC: deadline is aug 26th, is waiting on 
    - [x] new pipeline: https://github.com/matplotlib/matplotlib/pull/28658
    - [x] colormaps: https://github.com/matplotlib/matplotlib/pull/28454
- [x] [name=story645] docs:
  - [access to analytics](https://github.com/matplotlib/matplotlib/issues/28696)
  - new user survey ran by Jerome (@jeromefv-former GSOD) and Tammy (@tgmiller5)
- [x] NF Project summit 
    - Cambridge Mass, Sep 5-7
- [x] Small dev grant CFP - due Sep 30, 2024
    - possibly survey + doc reorg

### New business

- [name=story645][seperate hatch and egde color](https://github.com/matplotlib/matplotlib/pull/28104)
- [name=QuLogic] home page translations: [reST-ification](https://github.com/matplotlib/mpl-brochure-site/pull/96), [enable sphinx-intl](https://github.com/matplotlib/mpl-brochure-site/pull/97)
- [name=QuLogic] asyncio-based backends [PyGObject MR](https://gitlab.gnome.org/GNOME/pygobject/-/merge_requests/189)

## Notes
### GSOC
#### dev docs not building/updating
- known bug with a unit example 
- quick fix is to ban numpy2.1.0

#### new pipeline
 - has PR to @trygve's branch to adjust inheretance so to avoid breaking user code
     - will merge + add some more comment
 - when ScalarMappable is removed, methods can move down to `ColorizingArtist`

#### color map PR

#### Current state of things

 - https://trygvrad.github.io/gsoc-2024-bivariate-colormaps-summary/
 - need first 2 steps are there PRs, need 3 more to get everything landed

### RSE updates
 - kyle: data prototype stuff
     - working on patches
     - looking at numpy problems with docs build
     - gsoc
 - Elliott:
     - pybind11 work
     - working on ft2font
     - work on brochure site
 - Tom:
     - mostly review
     - trying to test with cp313t
         - the borrowed c++ refs may go away with pybind11
         - dragons may be in macos backend
 ### analytics
  - now public

### survey 

- need to see the questions + pre-design of analysis before it goes out

### summit
sending and 


- question about GDPR + discourse
    - can we move our users + history to another instance
- status of NF CoC for projects

### small development grant 
- not this cycle 

### hatchcolor/edgecolor
- hatchcolor + pcolor needs to be optional 
- need to make backends forgiving for backends that don't implement hatch 



# Aug 15th
_attending_: @efiring, @ksunden, @QuLogic, @story645, @trygvrad, @tgmiller5 

### Old business
- [ ] RSE
- [ ] GSOC: deadline is aug 26th, is waiting on 
    - [ ] new pipeline: https://github.com/matplotlib/matplotlib/pull/28658
    - [ ] colormaps: https://github.com/matplotlib/matplotlib/pull/28454

### New business
- [x] [name=story645] docs meeting:
  - [access to analytics](https://github.com/matplotlib/matplotlib/issues/28696)
  - new user survey ran by Jerome (@jeromefv-former GSOD) and Tammy (@tgmiller5)
- [x] NF Project summit 
    - Cambridge Mass, Sep 5-7
- [x] Small dev grant CFP - due Sep 30, 2024
    - possibly survey + doc reorg
  
### Pull requests 

## Notes

# user surve + analytics
- [x] follow-up email sent to steering council

# GSOC
- multivariate/bivariate needs approval
- pipeline: address reviews then changes
- potential tracking issue for rest of transition

# RSE
- fixing CI + getting 3.9.2 + pybind

# Aug 8
_attending_: @IGuKs80UTJCig4yt6Zos7w (greglucas), @story645, @tacaswell, @ksunden, @QuLogic, @QWhXj01mSwmTjk5kN1H_qQ(efiring), @trygvrad

## Agenda
### Old business
- [ ] RSE
- [ ] GSOC
    - ScalarMappable|shim|Colorizer boundaries/ seperation of concerns

### New business
- [name=story645] docs meeting: 
    - access to analytics 
    - new user survey
- windows wheel issue
- 
### Pull requests:
- [Build for musllinux on ARM](https://github.com/matplotlib/matplotlib/pull/28592) - feedback requested (@oscargus: I know that we may not want to build for every combination of platforms, but not how it is determined. Also, currently it takes 97 minutes. If I join the call, will try to remember that, I can provide feedback. If not, I'd appreciate if someone can.)

## Notes

### Windows wheel issue
- think we understand the issue and have a draft PR to fix it
- think we understand:
    - GHA runners have a bunch of different dlls
    - the one that came up first in the PATH found the wrong dll
    - by specifying a path to delvewheel we should be able to fix it
- bad timing on a devlewheel problem where things changed between when we tested and when we released
    - delevwheel did a release between .post0 and .post1
- Ian has a draft PR in that needs to be tested
- Reached out to Steve Dower
    - reccomended that we statically link msvc40.dll
    - should only be done for wheels (not CF)
- may be wider issue as and it may come back later in other places, may want a shared wheel for this dll?
- issue with not finding dll
    - one way to fix is set `--vsenv` but it assumes that msvc is installed and what you want to use
    - meson tries to find any complier, falls back to looking for msvc (which is how it works for most dev machines)
    - if something happens to be on the path, meson uses that BUT those dlls are not on path at run time

TODO:
 - get static linking set up on CI
 - get those wheels tested
 - do 3.9.2 or 3.9.1.post2
     - enable py3.13 if 3.9.2 route, not if 3.9.1.post2 release
 - target close of business Friday

### musl arm
- OP followed up
- Kyle posted summary, inculding asking for volunteer
    - OP agreed to take role
    - please add comment to yaml
- delaying speed up until follow up PR
    - if it is a problem, we can evaluate how to fix it
- do we want to pay for native arm?
    - currently no, but maybe if we find a sponsor for it

### GSOC/colorizer

- has implemented new colorizer class
- need to agree on some names
- need typing
- need tests for new functionality
- put new class in new file
- do we want to move norms to `norms.py`
    - pro: better names
    - con: either deal with deprecation dance (and cost to other) or accept it lives in 2 places (forever?)
    - consenus is to do the move and keep the forwarding forever, but we need to get buy-in from Tim
    - de-document, do not type hint, maybe drop from `__all__`
    - [EDIT]: An issue has been opened here https://github.com/matplotlib/matplotlib/issues/28690

color
- put property forwarders on ColorizingArtist 

colorizingartist + forwarding functions class (scalarmappbleshim?colorizershim/interface)

moving norm and cmap attributes from an artist to a colorizer
- if you set a norm/cmap on artist, then sets it on colorizer
    - when we deprecate scalarmappble, 
    - will either remove the ability to set or 
- silently overwrite setting properties -> only happens if you explicitly opt into colorizer

-> set_norm: add *arg* for new colorizer, or use `set_colorizer`


# Aug 1
_attending_: @efiring, @tacaswell, @ksunden, @QuLogic, @trygve, @timhoffm, @ianthomas23, @story645  

## Agenda
### Old business
- [ ] RSE
- [ ] GSOC
    - [ ] [data->color pipeline](https://github.com/matplotlib/matplotlib/pull/28428) changes/rearch
### New business
 - [ ] windows 3.9.1 + nightly wheels broken https://github.com/matplotlib/matplotlib/issues/28551
 - [ ] 
## Notes

### Windows 3.9.1 + nightly (contourpy)
- try windows 3.9.0 w/ nightly wheels 

### GSOC: colormapping pipeline
- proposal is transition from $scalermappable: norm \circ cmap \circ data$ model to $mappable : data -> color$ model
- questions on how do we roll this out:
    - vector_* methods: changes are mostly at the backing artist layer (AxesImage, PatchCollection, etc...) so would require writing/maintaining shadow API of Axes.* methods and scalarmappable aware artists 
    - putting in a scalarmappable shim so that layer of public API is still available
    - pulling out an initial interface layer PR w/ minimal implementation + shims 
        - POC that shows that the new pipeline slots into the existing workflow cleanly
        - shepherded by @tacaswell and @timhoffm 
        - fold in colorbar in a later PR
- colorbar pointing to artist? [adding cbar to ScalerMappable](https://github.com/matplotlib/matplotlib/issues/25880)

# July 25
_attending_: @trygve @efiring @ksunden @story645 @tacaswell, @QuLogic   

## Agenda
### Old business
- [x] RSE
- [x] GSOC

### New business

### Issues

## Notes

### GSOC
 - waiting on review 
   - https://github.com/matplotlib/matplotlib/pull/28428
- second PR, introduces VectorMappable to replace ScalarMappbale 
- suggestion to have a higher-level wrapper that holds both the mappable and the colormap so that we can do coordinated updates
    - also gives an escape hatch to do direct data -> color (without being forced through our norm concept)
- if we are going to go this route, doing it now seems good
    - conflicts between availabilty vs GSOC timeline
- needs to do some review


### RSE
- Caswell
    - starting to do review again
- Kyle
    - start of text in the new system
        - text has a lot of options, most are missing
    - starting to think about documentation
    - reviews 
- Elliott
    - working through open PRs
    - 3.13 wheel PR is mostly ready
    - working on Agg pybind11
    - reviews

### SDG + CZI
 - got it, will start work soon
 - given no-cost extension from CZI

### mplplaybook

- down to adding 4 minutes to docs build
- [mpl-playback](https://github.com/matplotlib/matplotlib/pull/23441#issuecomment-2233128336)
- needs to not add to much time (less than 10 minutes)
    - docs CI should not become the bottle neck
- needs to not add too much weight to output
- should hook into the "release mode" machinery
- hold off on waiting for SG to release with their fix

### doc building
 - discussion of why we build docs with the oldest version of Python we support
 - will move to newest and see if we get speed ups

### tag protection rules
 - restirct push tags to (to-be-created release manager team)
 - have already added a manual review step before wheels are uploaded to pypi


# July 18
_attending_: @efiring, @ksunden, @QuLogic, @trygvrad, @story645, @rcomer 


## Agenda
### old business
- [x] RSE
- [x] GSOC

### New business
- [ ] scipy

### Issues 
- [ ] [mpl-playback](https://github.com/matplotlib/matplotlib/pull/23441#issuecomment-2233128336)

## Notes
### GSOC
- is at 2/4 PRs for mvp
    - [colormaps](https://github.com/matplotlib/matplotlib/pull/28454)
    - [vectormappable](https://github.com/matplotlib/matplotlib/pull/28428)
    - next: imshow w/ examples
- if `NormAndColor` mappable encapsulating color goes in (waiting on chat w/ @timhoffm) then can potentially hook in data and rgb interpolations
    - find better names 

### Scipy

# June 27
_attending_: @efiring, @tacaswell, @ksunden, @story645, @QuLogic 

## Agenda
### Old business
- [x] RSE
- [x] GSOC
    - Colormaps: https://github.com/matplotlib/matplotlib/pull/28454
    - VectorMappable: https://github.com/matplotlib/matplotlib/pull/28428
### New business
- [x] 3.9.1 schedule
- [ ] 3.10 priorities

## Notes
### GSOC
- PRs have been opened
    - discusions about the API
    - do we want to keep `ScalarMappable` around as anything other than a back-compat shim?
    - keeping vector and scalar versions independent leads to duplicated / parallel classes (like old Qt4/Qt5 classes)
    - some things that are currently ScalarMappable do not have sensible VectorMappable counter parts (e.g. contour)
- Try to get 's review of VectorMappable, otherwise normal PR rules

### RSE
- Kyle:
    - data prototype stuff, mostly fixed the units example
    - GSOC work
    - PR review
- Elliott:
    - mostly 3.9.1 things
    - moved some things from 3.9.2 to 3.9-doc
    - review 3.9.1 PRs, looking at axvspan autolimit regression
    - looked at CF build issues
- Tom
    - on vacation last week, catching up this week
    - some review, need to finish writing a grant report
    
### 3.10

- target early October 24
- goals
    - GSOC work landing (Kyle and Hannah)
    - image testing framework overhaul (Tom)
    - work on mplgui (Tom)
    - jupyter rfb backend landed (Elliott)
    - Elliott has a list of PRs
        - https://github.com/matplotlib/matplotlib/pull/23056
        - https://github.com/matplotlib/matplotlib/pull/23085
        - https://github.com/matplotlib/matplotlib/pull/24554
        - https://github.com/matplotlib/matplotlib/pull/24626
        - https://github.com/matplotlib/matplotlib/pull/24744
    - 


### 3.9.1 target
- tomorrow (June 28) target date

# June 20
_attending_: @trygve, @QuLogic, @ksunden, @story645 

### Old business

- [ ] RSE
- [x] GSOC

## Notes

### GSOC
- can add testing by introducing colorbar/norm first
- package $n \times m \times l$ array as a $n\times m$ array with dtype tuple of length l
    - pro: reduces input to 2D arrays for purpose of manipulation
    - con: may require extra copies 
    - check: how data space interpolation is handled    

### translation: 
#### cheatsheets:
- translating in a way where layout is respected 
- how do I? construction not universal 
- possibly examples or plot type gallery instead (for tooling)

#### brochure: 
- refactor into translation friendly version

#### contribute:
- maybe write a short version: https://numpy.org/contribute/

### brochure site
- news section: revive https://github.com/matplotlib/mpl-brochure-site/pull/17
    - only show entries w/ a publish tag?
    - do we want to keep discourse?


# June 13
_attending_: 

## Agenda

### Old business
- [x] RSE
- [x] GSOC
- [x] SDG
- [ ][name=hannah][homepage translation](https://github.com/matplotlib/mpl-brochure-site/issues/93)
    - do we want to instead pilot the tooling on cheatsheets cause [demand](https://github.com/matplotlib/cheatsheets/pull/132)

### new business
 - [x] report from dev summit
 - [ ] plan for 3.9.1


## Notes

### dev summit

- about 40 people in Seattle
- lots of discussion about SPECs
    - https://scientific-python.org/specs/
    - endorsed the two we already do (timeline + uploading nightly wheels)
    - supply-chain related work relevant for us
    - other are not relevant
- talked with Thomas Fan about WASM builds
    - pyodide has updated build system so that projects can build
    - have it working again, but font loading is broken
        - our optimaztion settings make debugging hard (no symbols names)
    - cibuldwheel can build wasm "wheels" without patches (but does not work)
        - may need to be aware of filesystem sandbox

### RSE
 - SDG went
 - data prototype 

### GSOC
 - have a plan for how to organize PR in to work
 - ongoing discussions of code organizations

### 3.9.1 
 - a TK bug which has been fixed
 - sticky edges on bar bug (PR soon)
 - add back cm.get_cmap 
     - some users did not see warning
     - Tim has a PR to put it back
     - Greg and Tom say to put back temporarily
     - question about why users didn't see
         - Tom: is this due to the warning class we use that users never saw it
         - Greg: is this users jumping a bunch of versions
 - other color related questions (behavior of color maps with int intputs) https://github.com/matplotlib/matplotlib/issues/28198
 - should we also add `lut=` to the mapping registry version?

# ~~June 6~~ CANCELED 



# May 30 
_attending_: @efiring, @oceanwolf @QuLogic @tacaswell @story645 @IGuKs80UTJCig4yt6Zos7w (gregluca) @rcomer @ksunden 

## Agenda
### Old business
- [x] RSE
- [x] GSOC
- [x] SDG - due tomorrow 31st

### New Business
### Issues & PRs
- [ ] [name=hannah][homepage translation](https://github.com/matplotlib/mpl-brochure-site/issues/93)

## Notes
### RSE
- Elliott
    - SDG writing
    - reveiwing stalled new contributor PRs
    - finish some high-dpi fixes for cairo
- Kyle
    - thinking about grant stuff
    - some review
    - GSOC has started
- Tom
    - grant stuff
    - some issue review
    - work on grant reports

### GSOC
- breaking up current big PR into smaller chunks
- looking at git + rebasing tools to help with breaking up into parts

### SDG
 - has draft
 - adobe is adding support to add alttext to images
     - do what they do!
 - discussion of details of raqm / freetype interaction

### issues / PR
 - translating the brochure page
 - questions about how the tooling works
 - how do the translations get maintained going forward?
 - what is exit strategy?
 - is this actually of value to anyone?
 - @story645 will take point on sorting it out

### CF
- work still needs to be done for 3.9


# May 23
_attending_: @efiring, @ksunden @tacaswell @story645 @QuLogic 

## Agenda
### Old business
- [x] RSE updates
- [ ] SDG state
- [ ] ROSES state

### New business
- [ ] 3.9 release fallout?


## Notes
### RSE updates
 - Tom
     - avoid writing grants by responding to issues on GH
 - Kyle
     - also working on grant
     - issues on github

# May 16 
_attending_: @efiring, @QuLogic, @tacaswell, @ksunden, @story645 
## Agenda
### Old business
- [ ] RSE updates
- [x] GSOC update

### new business

- [x] 3.9 is out!
- [x] SDG followup


## Notes
### 3.9
 - we added an import that seems to break, but we think that is a local install issue.
- promote `:mpltype:` to be public (otherwise downstream packages that inherit our docstrings will break)
     - what else do we need to make public?
     - The set of thing that look like roles the show up in our source (generated via ``set($(ack ':[^:]*:`' -o -h --python).split())`` )
```
{'::`',
 ':align:`',
 ':alt:`',
 ':attr:`',
 ':caption:`',
 ':class:`',
 ':context:`',
 ':data:`',
 ':doc:`',
 ':download:`',
 ':envvar:`',
 ':file:`',
 ':format:`',
 ':func:`',
 ':height:`',
 ':include-source:`',
 ':math:`',
 ':mathmpl:`',
 ':meth:`',
 ':mod:`',
 ':mpltype:`',
 ':nofigs:`',
 ':program:`',
 ':rc:`',
 ':ref:`',
 ':scale:`',
 ':show-source-link:`',
 ':sup:`',
 ':target:`',
 ':width:`'}
```

We think only rc, or mpltype need to be moved up. (@qulogic will do).

## GSOC

- Had kickoff meeting before start of main coding period (starts week after next)
- need plan for how to get in
- maybe do not do auto inference at all
- how to handle complex data?
- sequencing
    - first PR: 1 norm, 1 colormap
    - follow on PR: additional colormaps
    - follow on PR: complex support
    - follow on PR: add more norms
    - follow on PR: how to combine VectorMappable and ScalarMappable?
- open questions
    - don't have "over" and "under" but still need "in bounds" vs "bad"
        - to handle out of bounds:
            - fixed color
            - pick "closest" point and use that
    - cartesian or polar coordinates in color space?
    - how to handle categorical
    - legend/colorbar


## SDG

- still being drafted
- focus on accessibility
    - embedding alt text into output meta-data (as discussed last week)
    - font overhaul work


## RSE update
 - Tom
     - grant work + avoiding grantwork by doing issue review
 - Kyle
     - some grant work, data prototype stuff
 - Elliott
     - Jury duty selectiono
     - 3.9 release 


# May 9
_attending_: @tacaswell, @greglucas, @QuLogic, @ksunden, @story645, @trygve

## Agenda
### Old Business
- [x] RSE
- [x] 3.9
- [ ] 3.10

### New Business
- [ ] [name=hannah][numfocus small dev grant](https://numfocus.typeform.com/to/mbtH7w) due May 31st

## Notes
### old business
 - Kyle
     - planning meeting for developer summit
     - meet with a NASA project on Monday
     - working on data prototype
     - helping with on 3.9 wrapup
 - Elliott
     - developer summit meeting
         - array protocol, supply chain validation work
     - 3.9 doc wrapup
     - mpl-sphinx-theme tagging
     - waiting for backports
     - maybe bug with old (>1yr) IPythons
     - tag today or tomorrow
 - Tom
     - mostly off

### small development grants
- Hannah will talk to Jni about feasibility of visual search
- hatches
- RFB work
- pull small/medium projects from CZI grant
    - saving alt text in image metadata
    - needs a plan for figuring out how screen readers read images
    - Elliot is drafting proposal


# May 2

_attending_: @tacaswell @story645 Ian Thomas @ksunden @QuLogic 

## Agenda
### Old Business
- [x] RSE
- [x] 3.9
- [ ] 3.10

### New Business

## Notes
### old business
#### RSE
 - Kyle
     - writing new NASA grant work
     - continuing interacitvity and contains in dataprototype
     - GSOC has been annouced, got 1 slot, need to reach out to start work
 - Elliott
     - reviewing Ian's PR
     - went through all the 3.9rc failures and opened issues or PRs for everything
     - working on getting api changes / whats new rolled up
     - do we want rc3?
         - IPython is happy without one
         - so no RC
     - planning meeting for scientific python developers summit tomorrwo
 - Tom
     - some issue/PR review
     - work on NASA grant.

### New business

#### anyone going to pycon
- Pavel (social media) and Chahak

#### IPython integration
 - almost done
 - last thing for 3.9 final

#### appveyor failures due to sphinx gallery
- due to upstream changes in sphinx/sphinx-gallery
- only see on appveyor because other CI systems do not install sphinx+sphinx-gallery
    - install from conda environment file
- PR existing to fix it (#28103)


# April 25

_attending_: @tacaswell @QWhXj01mSwmTjk5kN1H_qQ (Eric) @QuLogic @ksunden @story645 

## Agenda 
### Old Business
- [x] RSE updates
- [x] GSOC updates

### New Business
- [x] NASA propsoal
- [x] 3.9 status
- [ ] 3.10 piorities

## Notes
### RSE updates
- Kyle:
    - data prototype work, pushing on interactivity and contains
    - issue / PR work
    - some 3.9 issues down stream w/ Elliott
- Elliott:
    - catch up from vacation
    - no 3.9rc reports
        - do we know if it actually being tested?
    - ran rebuild in fedora
        - https://copr.fedorainfracloud.org/coprs/qulogic/mpl39/builds/ vs https://copr.fedorainfracloud.org/coprs/qulogic/mpl39.checker/builds/
        - only 10/130 new failures due to our RC
            - use of mpl.cm.get_cmap which was removed
            - use of plt.cm.get_cmap
            - new warning in python-mne (on legend with no entry)
            - mplcursors text changed, fixed upstream need a release
            - animatplot-ng sees effects of 3D limits change
            - may have broken pandas (preexisting unrelated failure on fedora, so did not test)
    - seaborn looks good with 3.9!
    - https://www.pepy.tech/projects/matplotlib?versions=3.8.4&versions=3.8.3&versions=3.8.2&versions=3.9.0rc2
- Tom
    - more progress on NASA grant

### GSOC

- have submited our ranking
- not heard anything back

### NASA
 - headline projects
     - cartopy to new data/artist model
         - work into how to integrate into existing structued data in that space
     - go all-in on pyodide (https://github.com/matplotlib/matplotlib/issues/27870)
         - https://github.com/pyodide/matplotlib-pyodide both agg and htmlCanvas backends exist
     - partner with a NASA mission to wrap interesting data
 - lots of maintence and support


### 3.10 priorities
 - colormapping work
 - 

     
# April 18

_attending_: @tacaswell @ksunden @QWhXj01mSwmTjk5kN1H_qQ (Efiring) @story645 

## Agenda

### Old business
- [ ] RSE

### New Business
- [x] [name=hannah] noting meeting attendance
- [ ] [name=hannah] [dedup hatch validation](https://github.com/matplotlib/matplotlib/pull/28076)

## Notes
### RSE
 - Tom:
     - grant work
     - issues review
 - Kyle
     - little bit of issues review
     - data prototype work

### attendance
Please remember to take attendance at meetings

### hatch validation
* https://github.com/matplotlib/matplotlib/pull/28076
 
 
### Data prototype

Just in time data + encoding and transform graph = visualizing large high dimensional multivariate datasets more consistently in less lines of code. 

just in time computation:
1. computational graph w/ delayed evaluation
2. querying and subsampling such that:
     1. computational datasets can be shown at various resolutions
     1. only subset needs to be loaded in memory/visualized

dynamic encoding:
1. more consistent way to give mappings in multiple artists ([Hullman & Qu](https://ieeexplore.ieee.org/abstract/document/8017651/))
2. treats the data fields more consistently with respect to encodings 

property syncing on artist:
1. artists can be reused
2. don't need to be manually updated individually 

why graph:
1. doing transformations, need to maintain/keep track of order for consistency
2. its inspectable in a way current isn't
3. can be broken down into smaller chunks, can add custom mapping
4. moves current implementation graph to data structure

tradeoff:
1. lots of encodings across different axes and artists - easier to reuse/share be
    * it's currently named different things in different artists
    * attaching the encoding function/mapping/$\nu$ to the artist
    * ex: color coding by category in line and scatter plot
    
Draw time querying + reducing the amount of info artists need to know about themselves facilitates real time data and reusing parts of the visualization. 

# April 11

_attending_: @tacaswell @jklymak @pXw4hSgTQF2--OciPYwa1w @QWhXj01mSwmTjk5kN1H_qQ (Anntzer), @IGuKs80UTJCig4yt6Zos7w (Efiring) @ksunden @QWhXj01mSwmTjk5kN1H_qQ 

## Agenda

### Old business
- [x] RSE updates
- [x] GSOC/GSOD

### New business
- [x] [name=tacaswell] default to RGBA stage interpolation https://github.com/matplotlib/matplotlib/issues/21167
- [ ] [name=saranti] [orientation parameter to violinplot](https://github.com/matplotlib/matplotlib/pull/27998)

## Notes
### grant recap
### RSE updates
 - Kyle
     - data prototype
         - clipping and images in new system
     - some 3.9
     - GSOC
 - Tom
     - grant stuff
     - review

### GSOC updates
 - reviews mostly done

### RGBA interpolation
- should remove clipping anyway
- should look Antony's suggestion of how to filter AA's data to clean up "fuzz" on constant data
- look into making the deault interplotaion stage depend on ratio between data pixels and screen pixels
- conclusion:
    - we will look at how to add an 'antialiased' interpolation stage
        - use same criteria as current antilaised flip
        - data space when upsampling
        - RGBA spacing when down sampling

# April 04
_attending_: @efiring, @ksunden, @tacaswell, @rcomer, @story645, @timhoffm, @QuLogic  

## Agenda
### Old business
- [x] RSE updates
- [x] GSOC / GSOD updates

### New business

- [x] 3.8.4 out!
- [x] 3.9.0 status?
- [x] NASA ROSES 2024 F7
- [ ] Colorbar snapping https://github.com/matplotlib/matplotlib/pull/26307

## Notes

### old
#### RSE updates

Kyle:
 - got 3.8.4 out
 - general review
 - data-prototype work
 - thinking about next NASA grant

Tom:
 - NASA grant
 - issue / bug review

Elliott:
 - prep for 3.9

#### GSOC / GSOD
 - missed GSOD deadline
 - GSOC
     - have 6 propsoals, look good
     - (not including detailed notes as these are public and do not want to break GSOC rules)
 - need more mentors
     
### new
#### 3.9.0rc status
 - was waiting on 3.8.x mergeup
 - should branch and tag today

#### NASA funding 
- trying to make formal friends
- looking for citations from all SMD
- looking for reviewers
- cartopy may also may be putting one in

#### singular colorbars
 - https://github.com/matplotlib/matplotlib/pull/26307#issuecomment-2038181561

     
# March 28
_attending_: @efiring, @ksunden, @story645, @trygvard, @QuLogic,

## Agenda

### old business

- [X] RSE updates
- [x] [name=hannah] GSOC apps due April 2nd, 1800UTC (next Tuesday)

### new business

- [ ] [name=ksunden] Last item I'd like for 3.8.4 [#27955](https://github.com/matplotlib/matplotlib/pull/27955)

## Notes

### RSE
- qulogic: working on Mac bugs; other PR reviews to finish off 3.9
- ksunden: also working on Mac bugs; tracking numpy 2; pybind11 fix for np2 released; all of blockers are gone for np2 micro-release; Ian released contourpy for np2; work on data prototype (lines, clipping, images); thinking about next NASA grant.

### New business




# March 21st

_attending_: @efiring, @ksunden, @QuLogic, @trygvard, @story645  

## Agenda

### old business

- [ ] RSE updates

### new business

- [ ] [name=timhoffm] https://github.com/matplotlib/matplotlib/pull/26307

## Notes

### RSE 
- qulogic: m1, pybind11, wrapping up 3.9, bouncing tasks to 3.10
- ksunden: 
    - pybind11, numpy 2.0, m1 (ksunden has it locally), 
    - dataprototype - dijkstra's algorithm & visualizing graph
- 3.9 : beta/rc soft deadline is next week 
- 3.8.4: numpy2.0 compliance, is on numpy timeline

### singular colorbars
- milestoned to 3.9, needs a decision from @tacaswell and @timhoffm 

### multivariate colorbars
- gsoc proposal draft, scope of project & components 

### 3.9 followups
- follow up about sphinx-tags multiline
- 

# March 14th

_attending_: @tacaswell, @efiring, @timhoffm, @QuLogic, @ksunden, @rcomer, @story645, @artemkislovskiy

## Agenda

### old business

- [x] RSE updates
- [ ] [name=hannah] steering council deadlines/turnaround
    - discuss at end of call
    
### new business
- [x] numpy 2.0 status
- [x] 3.8.4 release?
- [x] 3.9 status
- [x] [name=QuLogic] [Cursor coordinates on twinned Axes](https://github.com/matplotlib/matplotlib/pull/25556)
- [x] [name=QuLogic] [Avoiding levels in AutoDateLocator](https://github.com/matplotlib/matplotlib/issues/26363)
- [x] [name=QuLogic] [Decide what to do with `cycler` duplicates](https://github.com/matplotlib/matplotlib/issues/26868)
- [x] [name=QuLogic] [Return filename from save_figure](https://github.com/matplotlib/matplotlib/pull/27766)
- [x] [name=Hannah] [branch protection w/ labels](https://github.com/matplotlib/matplotlib/pull/27668)
- [x] [name=Tim] [Revert renaming labels to tick_labels in boxplot_stats()](https://github.com/matplotlib/matplotlib/pull/27916)

## Notes

### Intros

### RSE updates

- Elliott
  - mostly getting ready for 3.9
  - macos M1 CI jobs (lots of low tolerance image failures)
  - big triage push of 3.9 issues/PRs
      - took out 1/3, lots of docs left so not blockers for branching
  - pushed updates / rebases to existing PRs
- Kyle
    - 3.9 wrap up work
    - continuing work on data prototype work
    - numpy 2.0 fallout
        - mostly via pybind11, but may need to add a #define
        - some waiting on dependencies
        - in trianuglation and non-default contouring modes
- Tom
    - 3.9 help
    - issue/PR review

### numpy 2.0 status

- holding pattern for now

### 3.8.4 release

- main reason is for numpy
- waiting for pybind11 to sort some stuff out for 3.8.4rc

### PR review

- twinned axes cursors
   - https://github.com/matplotlib/matplotlib/pull/25556
   - last discussed 8mo ago
   - call likes the examples, will merge when test pass
- internals of autodatelocator logic
   - issue is if one of the levels is empty skip
   - API wise it makes sense to be able to skip levels
   - take propsoed patch, look into fallout in this particualr case off call
- two cyclers
    - we re-export `cycler` from `cycler` and we have a custom wrapper of `cycler` that does extra validation
    - also have a PR that cleans up imports and removes aliases
    - questions
        1. should we still have both?
        2. should we expose either
    - we do not use `plt.cycler` internally
        - is in a whats-new
    - our trend is to simplify so don't import
    - but pyplot should be mostly self-contained and a cycler is useful for setting rcparams
        - set_propcycle will make the cycler for you
        - on net, deprecate
    - consensus
        - deprecate, but be willing to back off if disruptive
- return value of toolbar.save_fig
    - nice way to do this (matches most dialog implementations):
        - `None` -> No file saved
        - SENTENIL -> can't tell if a file was saved
        - happy-path -> string to path
    - implementation (backwards compatible paranoid safe)
        - `None` -> don't know if a file was savef
        - SENTINEL -> actively did not save
        - happy-path -> string to path
    - currently return `None` everywhere
        - proposed implemenatio n
    - one usecase
        - https://github.com/kivy-garden/garden.matplotlib/blob/024d5c47f86577873de0939c169f369dd46ba595/backend_kivy.py#L939-L940\
    - consenus
        - go with the "nice way"
        - make sure API change note is clear that thrid-party backends will have to implement this
        - open an issue with Kivy backend when merged

- branch label rules
    - consenus
        - try it out
        - previously talked about on call and we agreed to do it
        - no user facing impact, low risk and we can always turn it off if we hate it
- bxp tick label revert
    - https://github.com/matplotlib/matplotlib/pull/27916
    - the parameter name and then key in the returned dict no longer match
    - attempt was made to replace dict with DataClass, but gets messy in this case
    - propsoal: 
        - leave bxp_stats alone
        - migrate to something more static in the future
    - consenus
        - go with this
        - also change the docstring to be clearer what it is

### SC timeline
- one week response window then ping once a week

# March 7th
_attending_: @tacaswell, @QWhXj01mSwmTjk5kN1H_qQ (efiring), @rcomer, @ksunden, @story645, @QuLogic, @timhoffm

## Agenda

### old business
- [x] RSE
- [x] 3.9

### new business
- [x] [name=tacaswell] grant updates
- [x] [name=hannah] triage team 

### Issues and PRs

## Notes


### RSE updates 

Kyle:
 - putting is scipy talk propsoal (on dataproto type)
 - data prototype work, thinking about Artist class tree
 - QoL improvements in repo to make less verbose
 - issue and PR review
 - pushing on yet more mac OSX segfaults / objectiveC level exceptions
     - new or pre-existing?  Hard to go back to old versions of OSX so very hard to debug
     - behavior is as documented, but did not notice this behavior before
         - only see when running as a subprocess, test was marked xfail because flaky, lightly tested / under used feature (singleshot timers), test sometimes passes before object crashes
         - subtle interaction with Python GC to produce an invalid pointer
Elliott:
 - Catching up from forced vacation
 - bit more pybind11 work (waiting for cgywin test to pass (just merged!))
 - started to work on performance benchmarks
     - working on windows + arm box

Tom:
 - some issue review + scipy talk discussions

### 3.9 updates

- worked on clearing out milestone yesterday
- no major items that should get a madrush to get in
- RC in 2 weeks
    - how does this interact with numpy 2.0
    - do not hold our RC for numpy beta
    - do another RC as soon as they have an RC
    - hold our 3.9 final for numpy2.0 rc
- david got new pydata sphinx theme working, please look at devdocs due to big changes in upstream themes
    - use social to drive eyeballs at this
    
### numpy 2.0

https://github.com/numpy/numpy/issues/25918#issuecomment-1980214917

- asking for sequence of:
  -  numpy beta
  -  mpl/scipy/... rc (of _something_)
  -  numpy rc
  -  mpl/scipy/... finals (of something)

### grant updates

### triage team

SC needs to be prompt or delegate authority

### repo to hold API automation from social

- good idea, start in @story645 's account and migrate when working


### DST is coming

Remember we follow the German schedule.

### rgba nan handling + extra copies

https://github.com/matplotlib/matplotlib/pull/27848


Conclusion: only copy if we have to mutate the user input

# 29 Feb 2024

_attending_: @ksunden, @QuLogic, @tacaswell, @story645 

## Agenda 

### old business
- [x] RSE reports
- [x] 3.9 progress

### new business

## Notes

### RSE report
- Tom: swamped with other work
- Kyle: 
    - preparing for scipy submissions
    - getting examples in data-prototype working again
    - issue triage / PR review
- Elliott:
    - on vacation
    - made progress on pybind11 work, no PR yet


### 3.9

- Still looking on target for RC in March 
- currently 73 open things in milestone

### numpy 2.0

- things are going slowly
- do micro release when rc to drop upper pin

# 22 Feb 2024

_attending_: @efiring, @ksunden, @QuLogic, @greglucas, @story645 

## Agenda

### Old business

- [x] RSE reports
- [x] 3.9 progress
- [x] scipy tutorial planning

### new business

## notes



### PRs
- [x] [name=hannah] [seperate edgecolor + hatchcolor](https://github.com/matplotlib/matplotlib/pull/26993)
## notes

### RSE reports
- ksunden: macOS, data prototype, general issue & PR review
- qulogic: pr review, finished animation->vid in docs (needs sphinx gallery reviews)

### separate edge + hatch

- setting hatch.color to 'inherit' from edgecolor 
    - needs an API behavior note probably
- use facecolor tracking edgecolor as model 
- on set alpha adjust hatch color? 
    - needs an API behavior note probably 
- setting alpha after setting edgecolor will overwrite current, preserve with users hatchcolor
- Check for parallel behavior, if possible, between Patch and Collection.

### side convo on hatch api
- figuring out which customizations to allow - color, density, etc
    - https://github.com/leejjoon/mpl-pe-pattern-usgs
    - https://github.com/leejjoon/mpl-pe-pattern-monster
- custom registry to allow strings but avoiding naming conflicts 
- similar to MarkerStyle -> HatchStyle
- SDG scope/level project

### pybind11 review
- can we go through w/ one proficient in pybind11 reviewer?
    - can we just get through with "is this ported correctly?"
- benchmarking? 