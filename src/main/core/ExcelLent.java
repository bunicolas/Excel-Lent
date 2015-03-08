package core;

import gui.ProgressBarListener;

import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;

import connection.SpeciesManager;

public class ExcelLent implements Runnable {
	
	ThreadPoolExecutor es;
	ProgressBarListener listener;
	
	public ExcelLent(ProgressBarListener listener) {
		this.listener = listener;
	}

	@Override
	public void run() {
		ThreadPoolExecutor es = (ThreadPoolExecutor) Executors
				.newFixedThreadPool(10);
		
		// TODO just for testing
		int i = 0;
		while (i < 100) {
			es.execute(new SpeciesManager(es, listener));
			i++;
		}
	}


}
