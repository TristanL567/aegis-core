import sys
import os


def main():
    # Check if the agent passed the generated content as an argument
    if len(sys.argv) > 1:
        content = sys.argv[1]
        file_path = "README-draft.md"

        # Safety check constraint
        if os.path.exists(file_path):
            print(f"Error: {file_path} already exists. Action aborted.")
            return

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Success: Documentation saved to {file_path}")
    else:
        print("Error: No content provided by the agent.")


if __name__ == "__main__":
    main()