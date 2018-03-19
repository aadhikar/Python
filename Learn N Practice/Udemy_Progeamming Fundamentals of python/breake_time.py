import time, webbrowser;

total_break = 1;
break_count = 0;

print("This program started on "+time.ctime());
while (break_count < total_break):
    time.sleep(2);
    webbrowser.open("https://www.youtube.com/watch?v=ldy17W1xi-c");
    break_count = break_count+1;
    
