from flask import Flask, render_template, send_from_directory
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def birthday_card():
    """Main route for the birthday card"""
    current_year = datetime.now().year
    age = current_year - 1994  # Born in 1994, so age will be 31 in 2025
    return render_template('birthday_card.html', age=age)

@app.route('/static/audio/<filename>')
def audio_file(filename):
    """Route to serve audio files securely"""
    try:
        return send_from_directory('static/audio', filename)
    except FileNotFoundError:
        return "Audio file not found", 404

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors gracefully"""
    return render_template('error.html', 
                         error_message="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors gracefully"""
    return render_template('error.html', 
                         error_message="Internal server error"), 500

if __name__ == '__main__':
    # Ensure audio directory exists
    audio_dir = os.path.join('static', 'audio')
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)
        print(f"Created audio directory: {audio_dir}")
        print("Please add your MP3 file as 'birthday_song.mp3' in the static/audio/ folder")
    
    # Check if birthday song exists
    birthday_song_path = os.path.join(audio_dir, 'birthday_song.mp3')
    if os.path.exists(birthday_song_path):
        print("✅ Birthday song found!")
    else:
        print("⚠️  Please add 'birthday_song.mp3' to the static/audio/ folder")
    
    print("🎉 Starting Kanchan Ji's Birthday Card Application...")
    print("🌐 Open http://localhost:5000 in your browser")
    print("💜 Happy 31st Birthday Kanchan Ji! 💜")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
