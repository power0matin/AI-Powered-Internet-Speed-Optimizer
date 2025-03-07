import React from 'react';

const SpeedTest = ({ onSpeedTest }) => {
    const handleSpeedTest = async () => {
        const response = await fetch('http://localhost:8000/speedtest');
        const data = await response.json();
        onSpeedTest(data);
    };

    return (
        <div>
            <button onClick={handleSpeedTest}>Run Speed Test</button>
        </div>
    );
};

export default SpeedTest;