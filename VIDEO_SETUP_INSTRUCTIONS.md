# 🎥 Video Background Setup Instructions

Your website is now configured to use a **video background** for the home page hero section! Here's how to add a free cooking video:

## Step 1: Download a Free Cooking Video

Visit one of these **100% free** stock video sites:

### 🌟 Recommended: Pexels (Easiest)
1. Go to: https://www.pexels.com/search/videos/cooking/
2. Search for videos like:
   - "chef dicing vegetables"
   - "cooking vegetables close up"
   - "knife chopping food"
   - "chef preparing food"
3. Find a video you like (15-30 seconds works best for looping)
4. Click the **Download** button
5. Select **HD** or **Full HD** quality (1080p recommended)

### Other Great Sources:
- **Pixabay**: https://pixabay.com/videos/search/cooking/
- **Mixkit**: https://mixkit.co/free-stock-video/cooking/
- **Coverr**: https://coverr.co/stock-video-footage/kitchen

## Step 2: Add Video to Your Project

1. Rename the downloaded video to: `cooking-video.mp4`
2. Place it in your `/static` folder
3. The file path should be: `/static/cooking-video.mp4`

## Step 3: Restart Your App

Restart the Flask app to see the video background in action!

## 🎬 Video Recommendations

**Best types of videos for background:**
- ✅ Close-up shots of cooking/dicing
- ✅ Slow motion chef preparing food
- ✅ Fire/flames from cooking
- ✅ Food being sautéed in a pan
- ✅ Vegetables being chopped
- ✅ 15-30 second clips (perfect for looping)

**Avoid:**
- ❌ Videos with text or logos
- ❌ Very long videos (loads slowly)
- ❌ Low quality/blurry footage

## 📐 Technical Details

The video will:
- ✅ Auto-play on page load (muted)
- ✅ Loop continuously
- ✅ Be darkened to 50% brightness (for text readability)
- ✅ Fallback to the static image if video fails to load
- ✅ Work on all devices (mobile & desktop)

## 🎨 Current Setup

- **Video path**: `/static/cooking-video.mp4`
- **Fallback image**: `/static/hero-cooking.jpg` (already in place)
- **Format**: MP4 (H.264 codec recommended for best compatibility)

---

**That's it!** Once you add the video file, your homepage will have a stunning, cinematic cooking video background. 🔥
