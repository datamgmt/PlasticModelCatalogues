program code(input,output);

const l = 5;
      ca:array[0..l-1] of integer = (3,7,9,3,7);

var d,I:integer;
    c,e:longint;
begin{code}
  writeln('Airfix catlogue number parity check digit generator.');
  writeln('Enter five digit catalogue number to get parity check digit.');
  writeln('Enter negative number to exit program.');
  writeln('For catalogue code ABCDE-F, then F = (7A+3B+9C+7D+3E) modulo 10.');
  writeln('Copyright (c) 2013 Steven S. Pietrobon. Version 1.0 14 Mar 2013.');
  writeln;
  repeat
    write('Enter code: ');
    readln(c);
    e := c;
    d := 0;
    if c > 0 then
      begin{valid code}
        for I := 0 to l-1 do
          begin{find code}
            d := d + (c mod 10)*ca[I];
            c := c div 10;
          end;{find code}
        write('Code = ');
        if e < 10000 then
          write('0');
        writeln(e:1,'-',(d mod 10):1);
        writeln;
      end;{valid code}
  until e < 0;
end.{code}