module code_df_tb();
reg net_f_sa0,A,B,C,D;
wire Z,Z_sa0;
code_df f(Z,Z_sa0,net_f_sa0,A,B,C,D);
initial
begin
net_f_sa0=1'b0; A=1'b0; B=1'b0; C=1'b0; D=1'b0;
#10 net_f_sa0=1'b0; A=1'b0; B=1'b0; C=1'b0; D=1'b1;
#10 net_f_sa0=1'b0; A=1'b0; B=1'b0; C=1'b1; D=1'b0;
#10 net_f_sa0=1'b0; A=1'b0; B=1'b0; C=1'b1; D=1'b1;
#10 net_f_sa0=1'b0; A=1'b0; B=1'b1; C=1'b0; D=1'b0;
#10 net_f_sa0=1'b0; A=1'b0; B=1'b1; C=1'b0; D=1'b1;
#10 net_f_sa0=1'b0; A=1'b0; B=1'b1; C=1'b1; D=1'b0;
#10 net_f_sa0=1'b0; A=1'b0; B=1'b1; C=1'b1; D=1'b1;
#10 net_f_sa0=1'b0; A=1'b1; B=1'b0; C=1'b0; D=1'b0;
#10 net_f_sa0=1'b0; A=1'b1; B=1'b0; C=1'b0; D=1'b1;
#10 net_f_sa0=1'b0; A=1'b1; B=1'b0; C=1'b1; D=1'b0;
#10 net_f_sa0=1'b0; A=1'b1; B=1'b0; C=1'b1; D=1'b1;
#10 net_f_sa0=1'b0; A=1'b1; B=1'b1; C=1'b0; D=1'b0;
#10 net_f_sa0=1'b0; A=1'b1; B=1'b1; C=1'b0; D=1'b1;
#10 net_f_sa0=1'b0; A=1'b1; B=1'b1; C=1'b1; D=1'b0;
#10 net_f_sa0=1'b0; A=1'b1; B=1'b1; C=1'b1; D=1'b1;
#10 $stop;
end
endmodule