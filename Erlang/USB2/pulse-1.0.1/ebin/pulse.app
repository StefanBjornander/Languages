{application,pulse,
             [{description,"ProTest User Level Scheduler for Erlang"},
              {vsn,"1.0"},
              {modules,[pulse,pulse_sup,
			pulse_event,pulse_event_terminal,pulse_event_graph,
			pulse_instrument, metacall,
		        pulse_gen_server]},
              {registered,[pulse]},
              {applications,[kernel,stdlib]},
	      {env,[{document,[pulse,pulse_instrument]}]},
              {mod,{pulse,[]}}]}.

%% eqc is not in the application list, since starting eqc can be done
%% in two ways. One of which is not starting the application eqc.
