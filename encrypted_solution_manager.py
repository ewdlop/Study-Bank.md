"""
Encrypted Solution Manual Manager
Provides encryption and decryption functionality for solution manuals.
Uses Fernet symmetric encryption from the cryptography library.
"""

import json
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class EncryptedSolutionManager:
    """Manages encrypted solution manuals with password-based encryption."""
    
    def __init__(self, salt=None):
        """
        Initialize the manager with an optional salt.
        If no salt is provided, a default one is used.
        """
        if salt is None:
            # Default salt - in production, this should be randomly generated and stored
            self.salt = b'study_bank_salt_2025'
        else:
            self.salt = salt if isinstance(salt, bytes) else salt.encode()
    
    def _derive_key(self, password: str) -> bytes:
        """
        Derive an encryption key from a password using PBKDF2.
        
        Args:
            password: The password to derive the key from
            
        Returns:
            A 32-byte key suitable for Fernet encryption
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key
    
    def encrypt_solution(self, solution_data: dict, password: str) -> bytes:
        """
        Encrypt solution data with a password.
        
        Args:
            solution_data: Dictionary containing problems and solutions
            password: Password to encrypt with
            
        Returns:
            Encrypted data as bytes
        """
        key = self._derive_key(password)
        fernet = Fernet(key)
        
        # Convert solution data to JSON string
        json_data = json.dumps(solution_data, indent=2)
        
        # Encrypt the data
        encrypted_data = fernet.encrypt(json_data.encode())
        return encrypted_data
    
    def decrypt_solution(self, encrypted_data: bytes, password: str) -> dict:
        """
        Decrypt solution data with a password.
        
        Args:
            encrypted_data: Encrypted data as bytes
            password: Password to decrypt with
            
        Returns:
            Decrypted solution data as dictionary
            
        Raises:
            Exception: If decryption fails (wrong password or corrupted data)
        """
        key = self._derive_key(password)
        fernet = Fernet(key)
        
        try:
            # Decrypt the data
            decrypted_data = fernet.decrypt(encrypted_data)
            
            # Parse JSON
            solution_data = json.loads(decrypted_data.decode())
            return solution_data
        except Exception as e:
            raise Exception(f"Decryption failed: {str(e)}. Invalid password or corrupted data.")
    
    def save_encrypted_solution(self, solution_data: dict, password: str, filepath: str, verbose: bool = True):
        """
        Encrypt and save solution data to a file.
        
        Args:
            solution_data: Dictionary containing problems and solutions
            password: Password to encrypt with
            filepath: Path to save the encrypted file
            verbose: Whether to print success message (default: True)
        """
        encrypted_data = self.encrypt_solution(solution_data, password)
        
        # Save to file
        with open(filepath, 'wb') as f:
            f.write(encrypted_data)
        
        if verbose:
            print(f"Encrypted solution manual saved to: {filepath}")
    
    def load_encrypted_solution(self, filepath: str, password: str) -> dict:
        """
        Load and decrypt solution data from a file.
        
        Args:
            filepath: Path to the encrypted file
            password: Password to decrypt with
            
        Returns:
            Decrypted solution data as dictionary
        """
        # Load from file
        with open(filepath, 'rb') as f:
            encrypted_data = f.read()
        
        # Decrypt
        solution_data = self.decrypt_solution(encrypted_data, password)
        return solution_data


def create_sample_solution_manual():
    """
    Create a sample solution manual with various problem types.
    
    Returns:
        Dictionary containing sample problems and solutions
    """
    solution_manual = {
        "title": "Study Bank Solution Manual",
        "version": "1.0",
        "subjects": {
            "algebra": {
                "problems": [
                    {
                        "id": "alg_001",
                        "question": "Solve for x: 2x + 5 = 13",
                        "solution": "x = 4",
                        "steps": [
                            "2x + 5 = 13",
                            "2x = 13 - 5",
                            "2x = 8",
                            "x = 4"
                        ]
                    },
                    {
                        "id": "alg_002",
                        "question": "Solve for x: x^2 - 5x + 6 = 0",
                        "solution": "x = 2 or x = 3",
                        "steps": [
                            "x^2 - 5x + 6 = 0",
                            "(x - 2)(x - 3) = 0",
                            "x - 2 = 0 or x - 3 = 0",
                            "x = 2 or x = 3"
                        ]
                    }
                ]
            },
            "calculus": {
                "problems": [
                    {
                        "id": "calc_001",
                        "question": "Find the derivative of f(x) = x^3 + 2x^2 - 5x + 1",
                        "solution": "f'(x) = 3x^2 + 4x - 5",
                        "steps": [
                            "f(x) = x^3 + 2x^2 - 5x + 1",
                            "f'(x) = d/dx(x^3) + d/dx(2x^2) - d/dx(5x) + d/dx(1)",
                            "f'(x) = 3x^2 + 4x - 5 + 0",
                            "f'(x) = 3x^2 + 4x - 5"
                        ]
                    }
                ]
            },
            "binary_operations": {
                "problems": [
                    {
                        "id": "bin_001",
                        "question": "Convert binary 10110101 to decimal",
                        "solution": "181",
                        "steps": [
                            "10110101 = 1×2^7 + 0×2^6 + 1×2^5 + 1×2^4 + 0×2^3 + 1×2^2 + 0×2^1 + 1×2^0",
                            "= 128 + 0 + 32 + 16 + 0 + 4 + 0 + 1",
                            "= 181"
                        ]
                    }
                ]
            }
        },
        "notes": "This is an encrypted solution manual. Keep the password secure."
    }
    
    return solution_manual


if __name__ == "__main__":
    # Demo usage
    print("=== Encrypted Solution Manual Demo ===\n")
    
    # Create manager
    manager = EncryptedSolutionManager()
    
    # Create sample solution manual
    print("Creating sample solution manual...")
    solution_data = create_sample_solution_manual()
    
    # Define password
    password = "secure_teacher_password_123"
    
    # Encrypt and save
    print("Encrypting and saving solution manual...")
    manager.save_encrypted_solution(
        solution_data, 
        password, 
        "encrypted_solutions.dat"
    )
    
    # Load and decrypt
    print("\nLoading and decrypting solution manual...")
    loaded_data = manager.load_encrypted_solution(
        "encrypted_solutions.dat", 
        password
    )
    
    print("\n=== Decrypted Solution Manual ===")
    print(f"Title: {loaded_data['title']}")
    print(f"Version: {loaded_data['version']}")
    print(f"\nSubjects available: {', '.join(loaded_data['subjects'].keys())}")
    
    print("\n=== Sample Problem ===")
    algebra_problem = loaded_data['subjects']['algebra']['problems'][0]
    print(f"ID: {algebra_problem['id']}")
    print(f"Question: {algebra_problem['question']}")
    print(f"Solution: {algebra_problem['solution']}")
    print("Steps:")
    for i, step in enumerate(algebra_problem['steps'], 1):
        print(f"  {i}. {step}")
    
    # Test wrong password
    print("\n=== Testing Wrong Password ===")
    try:
        manager.load_encrypted_solution("encrypted_solutions.dat", "wrong_password")
    except Exception as e:
        print(f"✓ Correctly rejected wrong password: {e}")
    
    print("\n=== Demo Complete ===")
