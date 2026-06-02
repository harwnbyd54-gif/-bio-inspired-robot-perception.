"""
================================================================================
Title: Bio-Inspired AI Robot: Pure Perception & Attention Tension Vectors
Platform: Designed for Kaggle / Python 3 Environment
Author: AI Robot Cognitive Architecture
================================================================================
"""

import numpy as np
import random
import time
import pandas as pd

class CognitiveAIEngine:
    """
    An advanced cognitive architecture simulating robotic consciousness using 
    Pure Perception, Attention Tension Vectors, and Dual-Layer Auditory Systems.
    """
    def __init__(self):
        # Kinematic tuning weight for immediate braking response
        self.danger_threshold_weight = 5.0
        
        # Spatial Mind Coordinates (The center point of the Robot's focus grid)
        self.mind_pos = np.array([400.0, 300.0])
        
        # Surrounding Environmental Stimuli Setup
        self.stimuli = [
            {"name": "Sudden Danger", "pos": np.array([150.0, 150.0]), "importance": 12.0},
            {"name": "Primary Goal", "pos": np.array([650.0, 450.0]), "importance": 7.0},
            {"name": "Notification", "pos": np.array([600.0, 150.0]), "importance": 2.5}
        ]

    def process_mind_tick(self, front_distance, current_speed, sound_db, sound_word):
        """
        Processes one full clock cycle of the robot's integrated consciousness.
        """
        # 1. KINEMATIC BRAKE DECISION (Pure Perception Module)
        # Bypasses heavy analytical logging, connecting input directly to action
        risk_index = (current_speed / front_distance) * self.danger_threshold_weight
        brake_decision = "⚠️ BRAKE ENGAGED" if risk_index > 1.0 else "✅ CONTINUE MOVE"
        
        # 2. AUDITORY AWARENESS CLASSIFIER (Passive vs Active Layer)
        # Prevents computational bloat by staying in a low-energy Zen-state
        SOUND_THRESHOLD = 70
        is_active_listening = (sound_db > SOUND_THRESHOLD) or (sound_word == "Keyword Identified")
        hearing_mode = "Active Listening (NLP Status)" if is_active_listening else "Passive Hearing (Zen State)"
        
        # Calculate Audio Attention Tension Vector boost based on signal severity
        if sound_word == "Keyword Identified":
            audio_tension_boost = 25.0  # Dominates cognitive priority
        elif is_active_listening:
            audio_tension_boost = (sound_db - SOUND_THRESHOLD) * 1.5
        else:
            audio_tension_boost = 0.0

        # 3. ATTENTION TENSION VECTOR OPTIMIZATION
        # Mathematical modeling of mind focus distribution using Euclidean distance
        highest_tension = -1
        focused_target = "None"
        
        # Map and evaluate spatial elements
        for s in self.stimuli:
            distance_px = np.linalg.norm(self.mind_pos - s["pos"])
            tension = (s["importance"] / (distance_px + 0.1)) * 100
            
            if tension > highest_tension:
                highest_tension = tension
                focused_target = s["name"]
                
        # Check if the sudden Auditory Event overrides spatial attention
        if audio_tension_boost > highest_tension:
            highest_tension = audio_tension_boost
            focused_target = f"Audio Event: [{sound_word}]"

        # 4. GENERATE TELEMETRY DICTIONARY
        return {
            "Distance (cm)": front_distance,
            "Speed (km/h)": current_speed,
            "Sound (dB)": sound_db,
            "Audio Content": sound_word,
            "Hearing Mode": hearing_mode,
            "Kinematic Action": brake_decision,
            "Max Tension": round(highest_tension, 2),
            "Mind Focal Lock": focused_target
        }

# ================================================================================
# SIMULATION DEPLOYMENT EXECUTION
# ================================================================================
if __name__ == "__main__":
    print("🤖 Initializing AI Brain Integration Engine...")
    ai_brain = CognitiveAIEngine()
    
    # Defining 4 diverse environmental scenarios to showcase multi-dimensional awareness
    scenarios = [
        {"dist": 35, "speed": 12, "db": 40, "word": "Ambient Wind"},      # 1. Normal exploration
        {"dist": 8,  "speed": 25, "db": 45, "word": "Silence"},           # 2. Kinematic critical risk
        {"dist": 40, "speed": 10, "db": 85, "word": "Loud Static"},       # 3. High Decibel Alert
        {"dist": 30, "speed": 15, "db": 55, "word": "Keyword Identified"}  # 4. Cognitive Language Trigger
    ]
    
    results = []
    for sc in scenarios:
        tick_data = ai_brain.process_mind_tick(sc["dist"], sc["speed"], sc["db"], sc["word"])
        results.append(tick_data)
        
    # Convert results into a beautiful Pandas DataFrame for professional telemetry display
    df_telemetry = pd.DataFrame(results)
    
    print("\n📊 --- COGNITIVE AI TELEMETRY SIMULATION RESULTS ---")
    # Setting pandas options to view all columns cleanly in the console
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    print(df_telemetry)
    
    print("\n💡 Scientific Conclusion:")
    print("-> Vectorized attention formula maps mental priorities in O(N) algorithmic complexity.")
    print("-> Passive Hearing threshold 
