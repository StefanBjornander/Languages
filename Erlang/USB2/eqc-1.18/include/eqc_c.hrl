
-record(ptr, {type = void, value}).

-import(eqc_c,
        [ start/1, start/2, start/3
        , stop/0, restart/0
        , free/1
        , create_array/2
        , read_array/2
        , store_array/2
        , read_string/1
        , create_string/1
        , array_index/2, array_index/3
        , deref/1
        , alloc/2
        , store/2
        , cast_ptr/2
        , add_to_ptr/2
        , sizeof/1
        ]).

