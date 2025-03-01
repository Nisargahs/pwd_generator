values=["i=20#v=40#p=5.5","i=35#v=22#p=3.4","i=43#v=34#p=5.8"]
i_avg=0 ; v_avg=0 ; p_avg=0 

for val in values:
    i_value,v_value,p_value=val.split("#")
    i_avg += float(i_value.split("=")[-1])
    v_avg += float(v_value.split("=")[-1])
    p_avg += float(p_value.split("=")[-1])

print(f"i_avg={i_avg/len(values)},v_avg={v_avg/len(values)},p_avg={i_avg/len(values)}")

