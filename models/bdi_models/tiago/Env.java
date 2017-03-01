// Environment code for project tiago.mas2j

import jason.asSyntax.*;
import jason.environment.*;
import java.util.logging.*;
import java.util.Random;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import jason.NoValueException;

public class Env extends Environment {

    private Logger logger = Logger.getLogger("tiago.mas2j."+Env.class.getName());
	private int robot_timer= 0;

	

    /** Called before the MAS execution with the args informed in .mas2j */
    @Override
    public void init(String[] args) {
    }

	@Override
	public boolean executeAction(String agName, Structure action) {
		/** The robot code's internal actions **/
		if (action.getFunctor().equals("add_time")) {
			try{
				robot_timer = robot_timer + (int)((NumberTerm)action.getTerm(0)).solve();
			}catch(NoValueException e){
			}
			return true;
		} 
		else if (action.getFunctor().equals("check_time")) {
			try{
				int thre = (int)((NumberTerm)action.getTerm(0)).solve();
				if (robot_timer >= thre){	
					addPercept("robot_code",Literal.parseLiteral("timeout"));
				}
			}catch (NoValueException e){
			}
			return true;
		} 
		else if (action.getFunctor().startsWith("reset_time")) {
			robot_timer= 0;
			return true;
		}
 
/** The human's internal actions **/
		else if (action.getFunctor().startsWith("tofile")) {
			String th = action.getTerm(0).toString();
			th = th.substring(1, th.length( ) - 1);
			try{
				tofile(th);
			} catch (IOException e) {
			}
			return true;
		}
		
/** The meta internal actions **/
		else if (action.getFunctor().equals("get_beliefs")) {
			try{
				get_beliefs();
			} catch (IOException e){
			}
			return true;
		}
		else {	
			logger.info("executing: "+action+", but not implemented!");
			return false;
		}
    }
	
	void tofile(String str) throws IOException {
		FileWriter fw = new FileWriter("output.txt",true);
		
		fw.write(str+"\n");
		fw.close();
	}

	void get_beliefs() throws IOException {
		try(BufferedReader br = new BufferedReader(new FileReader("meta_orders.txt"))) {
			for(String line; (line = br.readLine()) != null; ) {
				if (line != ""){
					addPercept("human",Literal.parseLiteral(line));
				}
			}
		}catch (IOException e) {
		}
	}

    /** Called before the end of MAS execution */
    @Override
    public void stop() {
        super.stop();
    }
}

