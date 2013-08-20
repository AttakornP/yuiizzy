from buildbot.changes.gitpoller import GitPoller
from buildbot.changes import filter
from buildbot.schedulers.basic import SingleBranchScheduler

#select project's settings to buildbot config.
from buildbot_config.settings.settings_hobby import BRANCH, PROJECT_NAME, PROJECT_CODE_URL, REPOSITORY_URL, WORKDIR

#builder name for this project.
builder_names = ['builder-pg']
gitpoller = GitPoller(REPOSITORY_URL
        , project=PROJECT_NAME
        , branch=BRANCH
        , pollinterval=30
        , workdir=WORKDIR
    )
#scheduler for buildbot.
change_filter = filter.ChangeFilter(project=PROJECT_NAME, branch=BRANCH)
scheduler = SingleBranchScheduler(name="hobby-develop-change"
        , change_filter = change_filter
        , treeStableTimer=30
        , builderNames=builder_names
    )
