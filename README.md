# Scrapinghub CLI



### Start using



```
$ shub-cli repl
$ shub-cli -api 'v65a787a987k08k9s797d7s8l98298sw' -project '89090' repl

```


### Usage:

```
$ shub-cli repl

> jobs [-tags tag1,] [-lacks tag1,] [-spider spider] [-state state] [-count count]
> job -id <id>
```

### Examples:

```
$ shub-cli repl
> jobs -count 100
> jobs -tags fast,production -lacks consumed,dev -spider spider1 -state finished
> job -id '10/10/1000'
```

### Help:
For help using this tool, please open an issue on the Github repository.