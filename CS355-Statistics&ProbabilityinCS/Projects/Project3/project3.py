import numpy.random as r
import statistics as s

TRIALS = 10000

def bounds(value, m, d):
    if(value < (m - (3 * d))):
        value = (m - (3 * d))
    elif(value > (m + (3 * d))):
        value = (m - (3 * d))
    else:
        value = value
    return value

def airlineOne(startTime, mu, delta):
    stranded = 0
    q2 = 0
    arrivaltime = startTime

    for i in range(TRIALS):
        val = startTime
        wait = 0

        if(startTime <= 480):

            ftime = bounds((r.normal(mu, delta)), mu, delta)
            val = val + (ftime + wait)

        if((val > 480) and (val <= (13*60))):
            
            if(val < (12.5*60)):
                wait = ((12.5*60) - val)
            else:
                wait = ((13*60) - val)
            
            ftime = bounds((r.normal(mu, delta)), mu, delta)
            val = val + (ftime + wait)
        elif(val > (13*60)):
            stranded += 1
            val = 0
            continue

        if((val > (13*60)) and (startTime <= (18*60))):

            if(val < (17*60)):
                wait = ((17*60) - val)
            elif(val < (17.5*60)):
                wait = ((17.5*60) - val)
            else:
                wait = ((18*60) - val)
            
            ftime = bounds((r.normal((mu-30), delta)), mu, delta)
            val = val + (ftime + wait)
        elif(val > (18*60)):
            stranded += 1
            val = 0
            continue
        
        if(val < (21*60)):
            q2 += 1

        arrivaltime += (val /60)
    
    print("\nAirline 1")
    print("Average arrival time =", round((arrivaltime / TRIALS), 2))
    print("P(Arriving <= 21:00) =", round(100*(q2/TRIALS), 2), "%")
    print("P(Stranded by airline 1) =", round(100*(stranded / TRIALS), 2), "%")
    return arrivaltime

def airlineTwo(startTime, mu, delta):
    stranded = 0
    q2 = 0
    arrivaltime = startTime
    for i in range(TRIALS):
        val = startTime
        wait = 0

        if(startTime <= 480):

            ftime = bounds((r.normal(mu, delta)), mu, delta)
            val = val + (ftime + wait)

        if((val > 480) and (val <= (12.5*60))):

            if(val < (12*60)):
                wait = ((12*60) - val)
            else:
                wait = ((12.5*60) - val)

            ftime = bounds((r.normal((mu+30), delta)), mu, delta)
            val = val + (ftime + wait)
        elif(val > (12.5*60)):
            stranded += 1
            val = 0
            continue

        if((val > (12.5*60)) and (startTime <= (17.5*60))):

            if(val < (16.5*60)):
                wait = ((16.5*60) - val)
            elif(val < (17*60)):
                wait = ((17*60) - val)
            else:
                wait = ((17.5*60) - val)

            ftime = bounds((r.normal(mu, delta)), mu, delta)
            val = val + (ftime + wait)
        elif(val > (17.5*60)):
            stranded += 1
            val = 0
            continue
        
        if(val  < (20.5*60)):
            q2 += 1

        arrivaltime += (val /60)

    print("\nAirline 2")
    print("Average arrival time =", round((arrivaltime / TRIALS), 2))
    print("P(Arriving <= 20:30) =", round(100*(q2/TRIALS), 2), "%")
    print("P(Stranded by airline 2) =", round(100*(stranded / TRIALS), 2), "%\n")
    return arrivaltime    

def main():
    airlineOne(480, 240, 24)
    airlineTwo(480, 210, 48)

if __name__ == "__main__":
    main()