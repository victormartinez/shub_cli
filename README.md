# Scrapinghub CLI
----
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

If you either do not want to configure the file or want to use non-default credentials start the shub-cli with the command:
```
$ shub-cli -api '<API KEY>' -project <PROJECT_ID> repl
```



### Quick Start:

```
$ shub-cli repl
```
or 

```
$ shub-cli -api '<API KEY>' -project <PROJECT_ID> repl
```

### Usage

##### Getting Jobs

```
> jobs [-tag tag] [-lacks tag] [-spider spider] [-state state] [-count count]
```

**Attention:** By default, shub-cli will prompt the last 10 jobs. To override that behaviour use the -count parameter with the number of jobs you intend to show.

##### Getting a specific job
```
> job -id <id>
```

##### Getting a specific job along with the logs
```
> job -id <id> --with-log
```


### Examples:

```
$ shub-cli repl

> jobs -count 100
> jobs -tag production -spider myspider -state finished
> job -id '10/10/1000'
```

### Help:
For help or suggestion please open an issue at the [Github Issues page](https://github.com/victormartinez/shub_cli/issues).
