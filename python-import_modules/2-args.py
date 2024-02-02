#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    def num_args():
        args = sys.argv
        num_args = len(args)
        if num_args == 1:
            print("0 arguments.")
        elif num_args == 2:
            print(f"{num_args - 1} argument:")
            print(f"argument 1: {args[1]}")
        else:
            print(f"{num_args - 1} arguments:")
        for i in range(1, num_args):
            print(f"{i}: {args[i]}")
num_args()
