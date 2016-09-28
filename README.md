# Scrapinghub CLI
----
A Command Line Interface at your hands to deal with the features of ScrapingHub.


![start-using](https://cloud.githubusercontent.com/assets/4680755/18898756/0ea42c0e-850a-11e6-801a-fdbd75915cdd.gif)


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

##### Getting a specific job
```
> job -id <id>
```

##### Getting a specific job along with the logs
```
> job -id <id> --with-logs
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