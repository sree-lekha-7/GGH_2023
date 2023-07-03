// net_f_sa0 is the node net_f when it is stuck-at 0.
// net_g_sa0 is the node net_g when net_f is stuck-at 0.
// Z_sa0 is the output when net_f is stuck-at 0.

module code_df(Z,Z_sa0,net_f_sa0,A,B,C,D);
input net_f_sa0,A,B,C,D;
output Z,Z_sa0;

assign net_e = A & B;
assign net_f = C | D;
assign net_g = ~ net_f;
assign Z = net_e ^ net_g;

assign net_g_sa0 = ~ net_f_sa0;
assign Z_sa0 = net_e ^ net_g_sa0;
endmodule
