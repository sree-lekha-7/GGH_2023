`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/02/2023 06:57:29 PM
// Design Name: 
// Module Name: code_df
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


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
