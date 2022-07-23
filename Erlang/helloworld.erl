-module(helloworld).

-export([hello_world/0]).
-export([clear/0]).

hello_world() -> io:format("Hello, Erlang!~n", []).
clear() -> io:format("\n").

%cd("c:/Users/stefa/Documents/Languages/Erlang").
%c(helloworld). helloworld:hello_world().
