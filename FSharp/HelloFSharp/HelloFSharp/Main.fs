// For more information see https://aka.ms/fsharp-console-apps

(*printf "Hello, "
//printfn "F#!"

let square n = n * n

let rec fib n =
  if n < 2
  then 1
  else fib (n - 2) + fib (n - 1)

let rec fib2 n = 
    match n with 
    | 0 -> 0 
    | 1 -> 1 
    | x -> fib2 (x - 2) + fib2 (x - 1) 

let rec fib3 = function 
    | 0 -> 0 
    | 1 -> 1 
    | x -> fib3 (x - 2) + fib3 (x - 1)

printfn "square %A, fibonacci %A" (square 2) (fib3 6)
*)

type Stack<'T> =
  | EmptyStack
  | RestStack of 'T * Stack<'T>

(*
let push value =
  function
    | EmptyStack -> RestStack (value, EmptyStack)
    | RestStack (v, r) -> RestStack (value, RestStack (v, r))
*)

let push value s =
  RestStack (value, s)

let top =
  function
    | EmptyStack -> failwith "Top: Empty Stack"
    | RestStack (v, _) -> v

let pop =
  function
    | EmptyStack -> failwith "Pop: Empty Stack"
    | RestStack (_, r) -> r

let rec printStack s = "[" + (printStackRecursive true s) + "]"
and printStackRecursive top =
  function
    | EmptyStack -> ""
    | RestStack (value, rest) -> (if top then "" else ",") + value.ToString() +
                                 (printStackRecursive false rest)

let s1 = push 1 (push 2 (push 3 EmptyStack))
printfn "Stack1: %s %A %s" (printStack s1) (top s1) (printStack (pop s1))

let s2 = pop s1
printfn "Stack2: %s %A %s" (printStack s2) (top s2) (printStack (pop s2))

let s3 = pop s2
printfn "Stack3: %s %A %s" (printStack s3) (top s3) (printStack (pop s3))

//let s4 = pop s3
//printfn "Stack4: %s %A %s" (printStack s4) (top s4) (printStack (pop s4))
printfn ""

type Queue<'T> =
  | EmptyQueue
  | RestQueue of 'T * Queue<'T>

let rec add value =
  function
    | EmptyQueue -> RestQueue (value, EmptyQueue)
    | RestQueue (v, r) -> RestQueue (v, add value r)

let first =
  function
    | EmptyQueue -> failwith "First: Empty Queue"
    | RestQueue (v, _) -> v

let remove =
  function
    | EmptyQueue -> failwith "Remove: Empty Queue"
    | RestQueue (_, r) -> r

let rec printQueue s = "[" + (printQueueRecursive true s) + "]"
and printQueueRecursive first =
  function
    | EmptyQueue -> ""
    | RestQueue (value, rest) -> (if first then "" else ",") + value.ToString() +
                                 (printQueueRecursive false rest)

let q1 = add 1 (add 2 (add 3 EmptyQueue))
printfn "Queue1: %s %A %s" (printQueue q1) (first q1) (printQueue (remove q1))

let q2 = remove q1
printfn "Queue2: %s %A %s" (printQueue q2) (first q2) (printQueue (remove q2))

let q3 = remove q2
printfn "Queue3: %s %A %s" (printQueue q3) (first q3) (printQueue (remove q3))

//let q4 = remove q3
//printfn "Queue4: %s %A %s" (printQueue q4) (first q4) (printQueue (remove q4))
printfn ""

type Map<'KeyType,'ValueType> =
  | EmptyMap
  | RestMap of ('KeyType * 'ValueType) * Map<'KeyType,'ValueType>

let rec put key value map =
  putX key value EmptyMap map

and putX key value rmap =
  function
    | EmptyMap -> (RestMap((key, value), rmap), None)
    | RestMap((oldkey, oldvalue), rest) when (key = oldkey) ->
             (merge rmap (RestMap((key, value), rest)), oldvalue)
    | RestMap(pair, rest) -> putX key value (RestMap(pair, rmap)) rest

and merge map =
  function
    | EmptyMap -> map
    | RestMap(pair, rest) -> RestMap(pair, merge map rest)

and exists key =
  function
    | EmptyMap -> false
    | RestMap((k, _), rest) when (k = key) -> true
    | RestMap(pair, rest) -> exists key rest

and lookup key =
  function
    | EmptyMap -> None
    | RestMap((k, v), rest) when (k = key) -> Some (v)
    | RestMap(_, rest) -> lookup key rest

and delete key map =
  deleteX key EmptyMap map
and deleteX key rmap =
  function
    | EmptyMap -> (rmap, None)
    | RestMap((oldkey, oldvalue), rest) when (key = oldkey) -> (merge rmap rest, oldvalue)
    | RestMap(pair, rest) -> deleteX key (RestMap(pair, rmap)) rest

and ToString s = "[" + (printMapRecursive true s) + "]"

and printMapRecursive first =
  function
    | EmptyMap -> ""
    | RestMap((key,value), rest) -> (if first then "" else ",") +
                                    "(" + key.ToString() + "," + value.ToString() + ")" +
                                    (printMapRecursive false rest)

let (m1, v1) = put 1 (Some("A")) EmptyMap
printfn "Map1: %s %A" (ToString m1) v1

let (m2, v2) = put 2 (Some("B")) m1
printfn "Map2: %s %A" (ToString m2) v2

let (m3, v3) = put 3 (Some("C")) m2
printfn "Map3: %s %A" (ToString m3) v3

let (m4, v4) = put 4 (Some("D")) m3
printfn "Map4: %s %A" (ToString m4) v4

let (m5, v5) = put 5 (Some("E")) m4
printfn "Map5: %s %A" (ToString m5) v5

printfn "Exists 0: %A" (exists 0 m5)
printfn "Exists 1: %A" (exists 1 m5)
printfn "Exists 2: %A" (exists 2 m5)
printfn "Exists 3: %A" (exists 3 m5)
printfn "Exists 4: %A" (exists 4 m5)
printfn "Exists 5: %A" (exists 5 m5)
printfn "Exists 6: %A" (exists 6 m5)

let (m11, v11) = put 1 (Some("X")) m5
printfn "Put 1 X: %s %A" (ToString m11) v11
let (m12, v12) = put 3 (Some("Y")) m5
printfn "Put 3 Y: %s %A" (ToString m12) v12
let (m13, v13) = put 5 (Some("Z")) m5
printfn "Put 5 Z: %s %A" (ToString m13) v13

printfn "Lookup 0: %A" (lookup 0 m5)
printfn "Lookup 1: %A" (lookup 1 m5)
printfn "Lookup 3: %A" (lookup 3 m5)
printfn "Lookup 5: %A" (lookup 5 m5)

let (m21, v21) = delete 1 m5
printfn "Delete 1: %s %A" (ToString m21) v21
let (m22, v22) = delete 3 m5
printfn "Delete 3: %s %A" (ToString m22) v22
let (m23, v23) = delete 5 m5
printfn "Delete 5: %s %A" (ToString m23) v23
let (m24, v24) = delete 0 m5
printfn "Delete 0: %s %A" (ToString m24) v24
