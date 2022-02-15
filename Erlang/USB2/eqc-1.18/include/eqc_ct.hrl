%% Macros for combination QuickCheck and Common Test

-define(quickcheck(Prop),
	case eqc:quickcheck(Prop) of
	  true -> 
            true;
	  false -> 
            case eqc:counterexample() of
                 undefined ->
                   exit(gave_up);
                 _ ->
                   exit(eqc:counterexample())
            end
	end).

