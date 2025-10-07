#!/usr/bin/env python3
"""
Biotech Clinical Trials Search Example

This script demonstrates how to search and analyze clinical trials
using OpenBB's biotech extension.

Usage:
    python biotech_trials_example.py

Requirements:
    pip install openbb[biotech]
"""

from openbb import obb


def main():
    """Main function to demonstrate biotech trial search."""
    
    print("=" * 60)
    print("OpenBB Biotech Extension - Clinical Trials Example")
    print("=" * 60)
    print()
    
    # Example 1: Search for cancer trials
    print("1. Searching for Phase 3 cancer trials...")
    print("-" * 60)
    
    try:
        cancer_trials = obb.biotech.trials.search(
            query="cancer",
            phase="3",
            status="recruiting",
            provider="clinicaltrials"
        )
        
        df = cancer_trials.to_dataframe()
        print(f"Found {len(df)} Phase 3 cancer trials currently recruiting\n")
        
        if len(df) > 0:
            print("First 5 trials:")
            print(df[['nct_id', 'title', 'sponsor', 'enrollment']].head())
            print()
            
            # Example 2: Get details for the first trial
            print("2. Getting detailed information for first trial...")
            print("-" * 60)
            
            nct_id = df.iloc[0]['nct_id']
            trial_details = obb.biotech.trials.details(
                nct_id=nct_id,
                provider="clinicaltrials"
            )
            
            details = trial_details.to_dict()['results'][0]
            print(f"NCT ID: {details['nct_id']}")
            print(f"Title: {details['title']}")
            print(f"Status: {details['status']}")
            print(f"Phase: {details['phase']}")
            print(f"Enrollment: {details['enrollment']}")
            print(f"\nBrief Summary:")
            print(details['brief_summary'][:500] + "..." if details['brief_summary'] else "N/A")
            print()
        
    except Exception as e:
        print(f"Error searching trials: {e}")
        print("Note: Make sure OpenBB biotech extension is installed:")
        print("  pip install openbb[biotech]")
        return
    
    # Example 3: Compare multiple indications
    print("3. Comparing trial counts across indications...")
    print("-" * 60)
    
    indications = ["diabetes", "alzheimer", "cardiovascular"]
    
    for indication in indications:
        try:
            trials = obb.biotech.trials.search(
                query=indication,
                phase="3",
                provider="clinicaltrials"
            )
            count = len(trials.to_dataframe())
            print(f"{indication.capitalize():20s}: {count:3d} Phase 3 trials")
        except Exception as e:
            print(f"{indication.capitalize():20s}: Error - {e}")
    
    print()
    print("=" * 60)
    print("Example completed successfully!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  - Explore more disease indications")
    print("  - Analyze trial success rates")
    print("  - Research company pipelines")
    print("  - See examples/biotechResearch.ipynb for more examples")
    print()


if __name__ == "__main__":
    main()
