import java.util.ArrayList;


class MatchResource {
    String resource ="/api/v1/backoffficeroles/getorganization/root";
    String[] list = new String[] {"/api/v1/backoffice/{}",
                                   "/api/v1/backoffice/role/{}",
                                   "/api/{}/backoffice/user/getone/{}",
                                   "/api/{}/{}/setup/{}/{}",
                                   "/api/{}/backoffice/user/{}/{}",
                                   "/api/v1/oms/orderinfo/{}/{}",
                                   "/api/v1/oms/{}/{}/{}",
                                   "/{}/{}/{}/{}/{}/{}",
                                   "/{}/{}/{}/getorganization/{}"};
    ArrayList<String> slices = new ArrayList<String>();
    ArrayList<String> possibilities = new ArrayList<String>();
    long _GLOBAL = 0;
    boolean access = false;
    String validate = "";
    String rSlice[] = resource.split("/",0); 
    long _INDEX;
    public static void main(String arg[]){
        // creating an object of MatchResource
        MatchResource M = new MatchResource();
        // shortlisting 
        long slashNo = M.resource.chars().filter(ch->ch == '/').count();
        // System.out.println(slashNo);
        // iterating the entire list
        for(int i=0; i<M.list.length; i++){
            long listSlashNo = M.list[i].chars().filter(ch->ch == '/').count();
            // shortlisting 
                        if(slashNo == listSlashNo){
                            // String rSliceCpy[] = M.rSlice;
                            // long curlyBraces = M.list[i].chars().filter(ch->ch == '{').count();
                            String lSlice[] = M.list[i].split("/",0);
                            long limit = M.rSlice.length - 1;
                            //String flag = "{}";
                            //System.out.println(M.list[i]);
                            //char flag = '{';
                            for(int j=1;j<=limit; j++){
                                    if(M.rSlice[j].equals(lSlice[j])){
                                        M._GLOBAL++;
                                    }
                                    else{
                                        if(lSlice[j].charAt(0) == '{'){
                                            M._GLOBAL++;
                                            
                                        }
                                    }
                                 } 
                                //System.out.println(limit);
                                         if(M._GLOBAL == limit ){
                                                //System.out.println(M.list[i]);
                                            M.possibilities.add(M.list[i]);
                                         }
                                
                                 M._GLOBAL = 0;                           
                             }      
        } // end of list iteration

        for(String s : M.possibilities){
            String cpy = s;
            long braces = cpy.chars().filter(ch->ch == '{').count();
            //System.out.println(" Limit of the loop = "+braces);
            //System.out.println(braces);
            for(int k=0; k<braces; k++){
                //System.out.println(" iterator = "+k);
                int index = cpy.indexOf('{');
               // System.out.println(index);
                //System.out.println(cpy.charAt(0));
               //System.out.println(cpy.substring(0,index-1));
               String temp = cpy.substring(0,index-1);
               if(!temp.equals("")){
                //System.out.println(temp);
                M.slices.add(temp);
               }
                cpy = cpy.substring(index+2);
            }
            for(String str : M.slices){
                if(M.resource.contains(str)){
                    M._INDEX++;
                }
            }
            if(M._INDEX == M.slices.size()){
                System.out.println(s);
            }
        }

       
    }
}