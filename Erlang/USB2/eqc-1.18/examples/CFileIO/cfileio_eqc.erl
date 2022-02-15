-module(cfileio_eqc).
-include_lib("eqc/include/eqc.hrl").
-include_lib("eqc/include/eqc_statem.hrl").
-compile(export_all).

% Model the C file system operations: read, seek, write,and eof

% These functions model the data in a file, with operations to insert
% and extract subsequences.

extract(L,Pos,Len) ->
    {_,X} = split(Pos,L),
    {Res,_} = split(Len,X),
    Res.

insert(L,Pos,Data) ->
    {Pre,X} = split(Pos,L),
    {_,Suf} = split(length(Data),X),
    extend(Pre,Pos,0)++Data++Suf.

split(N,L) ->
    case N > length(L) of
	true ->
	    {L,[]};
	false ->
	    lists:split(N,L)
    end.

extend(L,N,X) ->
    case length(L) < N of
	true ->
	    L ++ [X || _ <- lists:seq(1,N-length(L))];
	false ->
	    L
    end.

% Simple properties of insertion and extraction

prop_extract_insert() ->
    ?FORALL({L,Pos,Data},{list(char()),nat(),list(char())},
	    extract(insert(L,Pos,Data),Pos,length(Data)) == Data).

prop_insert_extract() ->
    ?FORALL(L,list(char()),
	    ?FORALL({Pos,Len},{choose(0,length(L)),nat()},
		    insert(L,Pos,extract(L,Pos,Len)) == L)).

% These functions define a state machine specification, as usual.
% They add specification of the file pointer position, the 
% eof flag, and reading/writing mode.

-record(c_file,{contents=[],position=0}).

initial_state() ->
    #c_file{}.

% The command generator.

command(S) ->
    oneof([{call,c,fread,[size()]},
	   {call,c,fwrite,[list(noshrink(choose(0,255)))]},
	   {call,c,fseek,[pos()]},
	   {call,c,feof,[]}]).

pos() -> nat().

size() -> nat().

% The state transition function.

next_state(S,_,{call,c,fread,[Size]}) ->
    #c_file{contents=L,position=Pos} = S,
    S#c_file{position = Pos + length(extract(L,Pos,Size))};
next_state(S,_,{call,c,fwrite,[Data]}) ->
    #c_file{contents=L,position=Pos} = S,
    S#c_file{contents=insert(L,Pos,Data),
	     position=Pos+length(Data)};
next_state(S,_,{call,c,fseek,[Pos]}) ->
    S#c_file{position=Pos};
next_state(S,_,_) ->
    S.

% Preconditions.

precondition(_,{call,_,_,_}) ->
    true.

% Postconditions check the results of each read, and the value of eof.

postcondition(S,{call,c,fread,[Size]},V) ->
    {N,Data} = V,
    #c_file{contents=L,position=Pos} = S,
    N == length(Data) andalso Data == extract(L,Pos,Size);
postcondition(S,{call,c,feof,[]},V) ->
    #c_file{contents=L,position=Pos} = S,
    (Pos > length(L)) == (V /= 0);
postcondition(_,{call,_,_,_},_) ->
    true.

% These functions define how operations in the state machine should
% be represented in C, and how the generated C code should be compiled
% and run.

compile(C,{call,c,fread,[Size]}) ->
    io:format(C,"TUPLE(INT(n=fread(buffer,1,~w,stream));"++
	              "LIST(for(i=0;i<n;i++) INT(buffer[i])));",
	      [Size]);
compile(C,{call,c,fwrite,[Data]}) ->
    if length(Data) > 0 ->
	    [io:format(C,"buffer[~w]=~w;",[I,D]) 
	     || {I,D} <- lists:zip(lists:seq(0,length(Data)-1),Data)];
       true ->
	    ok
    end,
    io:format(C,"INT(fwrite(buffer,1,~w,stream));",[length(Data)]);
compile(C,{call,c,fseek,[Pos]}) ->
    io:format(C,"INT(fseek(stream,~w,SEEK_SET))",[Pos]);
compile(C,{call,c,feof,[]}) ->
    io:format(C,"INT(feof(stream));",[]).

run(Cmds) ->
    {ok,C} = file:open("generated.c",[write]),
    [compile(C,Call) || {set,_,Call} <- Cmds],
    io:format(C,"~n",[]),
    ok = file:close(C),
    os:cmd("c:\\cygwin\\bin\\tcsh < runtest.csh"),
    file:delete("data.txt"),
    {ok,Vals} = file:consult("to_eqc.txt"),
    Vals.

% The property looks very like any other state machine property, with the
% exception that postconditions are checked after the commands are run.

prop_cfileio() ->
    ?FORALL(Cmds,commands(?MODULE),
	    begin
		Vals = run(Cmds),
		?WHENFAIL(io:format("~p~n",[Vals]),
			  postconditions(?MODULE,Cmds,Vals))
	    end).

