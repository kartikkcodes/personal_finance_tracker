#!/usr/bin/env python3
"""
Personal Finance Tracker - Nepal Edition

A comprehensive personal finance management application designed for Nepal,
with all amounts in Nepali Rupees (NPR) and localized features.

Author: Kartik Kandari
Date: June 2025
"""

import sys
import os

def display_welcome():
    """Display welcome screen"""
    print("\n" + "="*75)
    print("🏦" + " PERSONAL FINANCE TRACKER - NEPAL EDITION ".center(71) + "🏦")
    print("="*75)
    print("🇳🇵 Designed for Nepal - All amounts in Nepali Rupees (NPR)")
    print("📊 Track your income, expenses, and budgets effectively")
    print("📈 Generate beautiful reports and visualizations")
    print("💡 Make informed financial decisions")
    print("\n" + "="*75)

def display_menu():
    """Display main options"""
    print("\n🚀 GET STARTED:")
    print("-" * 40)
    print("1. 💼 START FINANCE TRACKER")
    print("   - Track your income and expenses")
    print("   - Set and monitor budgets")
    print("   - Generate financial reports")
    print("   - Create visualizations")
    print()
    print("2. ❌ EXIT")
    print("-" * 40)

def get_choice():
    """Get user choice with validation"""
    while True:
        try:
            choice = input("\n👆 Enter your choice (1 or 2): ").strip()
            if choice in ['1', '2']:
                return int(choice)
            else:
                print("❌ Please enter 1 or 2")
        except (ValueError, KeyboardInterrupt):
            print("\n👋 Namaste! Goodbye!")
            sys.exit(0)

def run_finance_tracker():
    """Run the finance tracker application"""
    print("\n💼 Starting Personal Finance Tracker...")
    print("🇳🇵 Ready to manage your finances in NPR")
    print("⏳ Loading...\n")
    
    try:
        from interactive_finance_tracker import main
        main()
    except ImportError as e:
        print(f"❌ Error importing finance tracker: {e}")
        print("💡 Make sure interactive_finance_tracker.py is in the same folder")
    except Exception as e:
        print(f"❌ Error running finance tracker: {e}")

def main():
    """Main launcher function"""
    try:
        while True:
            display_welcome()
            display_menu()
            choice = get_choice()
            
            if choice == 1:
                run_finance_tracker()
                print("\n💼 Finance tracker session ended.")
                restart = input("🔄 Do you want to start again? (y/n): ").strip().lower()
                if restart not in ['y', 'yes']:
                    break
            elif choice == 2:
                print("\n👋 Thank you for using Personal Finance Tracker!")
                print("🇳🇵 Namaste! Keep managing your finances wisely! 🌟")
                break
                
    except KeyboardInterrupt:
        print("\n\n👋 Namaste! Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("💡 Please check that all files are present and try again.")

if __name__ == "__main__":
    main()

