import React from 'react';
import SpeedTest from './components/SpeedTest';
import AIAnalysis from './components/AIAnalysis';
import Optimizations from './components/Optimizations';
import './App.css';

const App = () => {
    const [speedResult, setSpeedResult] = React.useState(null);

    const handleSpeedTest = (result) => {
        setSpeedResult(result);
    };

    return (
        <div className="App">
            <h1>Network Speed Test and Optimization Tool</h1>
            <SpeedTest onSpeedTest={handleSpeedTest} />
            {speedResult && <AIAnalysis speedResult={speedResult} />}
            <Optimizations />
        </div>
    );
};

export default App;