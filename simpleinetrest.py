def simInt(p, i, t):
    return (p * i * t) / 100

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 4:
        p = float(sys.argv[1])
        i = float(sys.argv[2])
        t = float(sys.argv[3])
        print("Simple Interest:", simInt(p, i, t))