#!/usr/bin/env python3
"""
Command-line interface for managing encrypted solution manuals.
Allows creating, viewing, and managing encrypted solution files.
"""

import argparse
import sys
import json
import getpass
from pathlib import Path
from encrypted_solution_manager import EncryptedSolutionManager, create_sample_solution_manual


def create_solution_manual(args):
    """Create a new encrypted solution manual."""
    manager = EncryptedSolutionManager()
    
    # Get password
    password = args.password
    if not password:
        password = getpass.getpass("Enter password for encryption: ")
        password_confirm = getpass.getpass("Confirm password: ")
        if password != password_confirm:
            print("Error: Passwords do not match!")
            sys.exit(1)
    
    # Load solution data from JSON file if provided, otherwise create sample
    if args.input:
        try:
            with open(args.input, 'r') as f:
                solution_data = json.load(f)
            print(f"Loaded solution data from: {args.input}")
        except Exception as e:
            print(f"Error loading input file: {e}")
            sys.exit(1)
    else:
        print("No input file provided. Creating sample solution manual...")
        solution_data = create_sample_solution_manual()
    
    # Encrypt and save
    try:
        manager.save_encrypted_solution(solution_data, password, args.output)
        print(f"✓ Successfully created encrypted solution manual: {args.output}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def view_solution_manual(args):
    """View an encrypted solution manual."""
    manager = EncryptedSolutionManager()
    
    # Get password
    password = args.password
    if not password:
        password = getpass.getpass("Enter password to decrypt: ")
    
    # Load and decrypt
    try:
        solution_data = manager.load_encrypted_solution(args.file, password)
        
        if args.format == 'json':
            # Output as JSON
            print(json.dumps(solution_data, indent=2))
        else:
            # Human-readable format
            print(f"\n{'='*60}")
            print(f"Title: {solution_data.get('title', 'Untitled')}")
            print(f"Version: {solution_data.get('version', 'N/A')}")
            print(f"{'='*60}\n")
            
            if 'subjects' in solution_data:
                for subject_name, subject_data in solution_data['subjects'].items():
                    print(f"\n{subject_name.upper()}")
                    print("-" * 40)
                    
                    if 'problems' in subject_data:
                        for problem in subject_data['problems']:
                            print(f"\nProblem ID: {problem.get('id', 'N/A')}")
                            print(f"Question: {problem.get('question', 'N/A')}")
                            print(f"Solution: {problem.get('solution', 'N/A')}")
                            
                            if 'steps' in problem and args.show_steps:
                                print("Steps:")
                                for i, step in enumerate(problem['steps'], 1):
                                    print(f"  {i}. {step}")
                            print()
            
            if 'notes' in solution_data:
                print(f"\n{'='*60}")
                print(f"Notes: {solution_data['notes']}")
                print(f"{'='*60}\n")
        
        print("✓ Successfully decrypted and displayed solution manual")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def export_solution_manual(args):
    """Export encrypted solution manual to plain JSON."""
    manager = EncryptedSolutionManager()
    
    # Get password
    password = args.password
    if not password:
        password = getpass.getpass("Enter password to decrypt: ")
    
    # Load and decrypt
    try:
        solution_data = manager.load_encrypted_solution(args.file, password)
        
        # Save to JSON file
        with open(args.output, 'w') as f:
            json.dump(solution_data, f, indent=2)
        
        print(f"✓ Successfully exported to: {args.output}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def verify_solution_manual(args):
    """Verify that an encrypted solution manual can be decrypted."""
    manager = EncryptedSolutionManager()
    
    # Get password
    password = args.password
    if not password:
        password = getpass.getpass("Enter password to verify: ")
    
    # Try to decrypt
    try:
        solution_data = manager.load_encrypted_solution(args.file, password)
        print(f"✓ Password is correct!")
        print(f"  Title: {solution_data.get('title', 'Untitled')}")
        print(f"  Version: {solution_data.get('version', 'N/A')}")
        if 'subjects' in solution_data:
            num_subjects = len(solution_data['subjects'])
            total_problems = sum(
                len(subject.get('problems', [])) 
                for subject in solution_data['subjects'].values()
            )
            print(f"  Subjects: {num_subjects}")
            print(f"  Total problems: {total_problems}")
    except Exception as e:
        print(f"✗ Password is incorrect or file is corrupted")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Manage encrypted solution manuals for Study Bank",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create a new encrypted solution manual with sample data
  %(prog)s create -o solutions.enc
  
  # Create from existing JSON file
  %(prog)s create -i my_solutions.json -o solutions.enc -p mypassword
  
  # View an encrypted solution manual
  %(prog)s view solutions.enc
  
  # View with solution steps
  %(prog)s view solutions.enc --show-steps
  
  # Export to plain JSON
  %(prog)s export solutions.enc -o solutions.json
  
  # Verify password
  %(prog)s verify solutions.enc
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new encrypted solution manual')
    create_parser.add_argument('-i', '--input', help='Input JSON file with solution data')
    create_parser.add_argument('-o', '--output', default='encrypted_solutions.dat',
                              help='Output encrypted file (default: encrypted_solutions.dat)')
    create_parser.add_argument('-p', '--password', help='Encryption password (will prompt if not provided)')
    create_parser.set_defaults(func=create_solution_manual)
    
    # View command
    view_parser = subparsers.add_parser('view', help='View an encrypted solution manual')
    view_parser.add_argument('file', help='Encrypted solution file')
    view_parser.add_argument('-p', '--password', help='Decryption password (will prompt if not provided)')
    view_parser.add_argument('--show-steps', action='store_true', help='Show solution steps')
    view_parser.add_argument('--format', choices=['text', 'json'], default='text',
                            help='Output format (default: text)')
    view_parser.set_defaults(func=view_solution_manual)
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export encrypted solution manual to JSON')
    export_parser.add_argument('file', help='Encrypted solution file')
    export_parser.add_argument('-o', '--output', required=True, help='Output JSON file')
    export_parser.add_argument('-p', '--password', help='Decryption password (will prompt if not provided)')
    export_parser.set_defaults(func=export_solution_manual)
    
    # Verify command
    verify_parser = subparsers.add_parser('verify', help='Verify password for encrypted solution manual')
    verify_parser.add_argument('file', help='Encrypted solution file')
    verify_parser.add_argument('-p', '--password', help='Password to verify (will prompt if not provided)')
    verify_parser.set_defaults(func=verify_solution_manual)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    args.func(args)


if __name__ == "__main__":
    main()
