# Scrapinghub CLI

A Command Line Interface at your hands to deal with the features of ScrapingHub.

[![Code Health](https://landscape.io/github/victormartinez/shub_cli/master/landscape.svg?style=flat)](https://landscape.io/github/victormartinez/shub_cli/master)


![start-using](https://cloud.githubusercontent.com/assets/4680755/18898756/0ea42c0e-850a-11e6-801a-fdbd75915cdd.gif)

### Install
You must install it through pip.

```
$ pip install shub-cli
```

### Configuration
Shub CLI will look for the `.scrapinghub.yml` created by [ScrapingHub](https://doc.scrapinghub.com/shub.html?highlight=yml#quickstart) in your home directory and read the default API_KEY and PROJECT_ID.
If you do not have that file, set it up according to the example below:

```
~/.scrapinghub.yml

apikeys:
  default: <API_KEY>
projects:
  default: <PROJECT_ID>
```

### Start

If you set up ~/.scrapinghub.yml file
```
$ shub-cli repl
```

Otherwise...
```
$ shub-cli -api <API KEY> -project <PROJECT_ID> repl
```

If you just want to run a command
```
$ shub-cli [credentials|spiders|job|jobs|schedule]
```


### Cheatsheet

```
> credentials
> spiders
> job [-show|-cancel|-delete id]
> jobs [-spider spider] [-tag tag] [-lacks tag] [-state state] [-count count]
> schedule [-spider spider] [-tags tag1,tag2] [-priority 1|2|3|4]
```


### Commands

#### Credentials

Check what credentials are being used to connect to Scrapinghub.
```
> credentials
```


#### Spiders
List all spiders available.
```
> spiders
```


#### Jobs

List the last 10 jobs or the ones according to your criteria.
```
> jobs
> jobs -spider example -tag production -lacks consumed -state finished -count 100
```

**Attention:** By default, shub-cli will prompt the last 10 jobs. To override that behaviour use the -count parameter with the number of jobs you intend to show.

#### Job

Show, delete or cancel a id.
```
> job -show <id>
> job -show <id> --with-log
> job -delete <id>
> job -cancel <id>
```


### Help:
For help or suggestion please open an issue at the [Github Issues page](https://github.com/victormartinez/shub_cli/issues).
